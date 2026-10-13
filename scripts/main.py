import os
import sys
import argparse
from load_env import load_env_file
from build_docs import BuildDocs
from send_docs import SendDocs

def parse_args():
    parser = argparse.ArgumentParser(
        description="DocOps Engine - Modular Technical & Architectural Documentation Compiler."
    )
    parser.add_argument(
        '--no-email', '--skip-email',
        dest='send_email',
        action='store_false',
        help='Compile Markdown and DOCX without sending email notification.'
    )
    parser.add_argument(
        '--send-email',
        dest='send_email',
        action='store_true',
        default=True,
        help='Compile documents and send email notification to stakeholders (default: True).'
    )
    parser.add_argument(
        '--email',
        type=lambda v: v.lower() in ('true', '1', 't', 'y', 'yes', 'sim', 's'),
        dest='email_flag',
        default=None,
        help='Enable or disable email dispatch (--email true / --email false).'
    )
    parser.add_argument(
        '--doc-dir',
        dest='doc_dir',
        default=None,
        help='Custom path to documentation folder containing topicos/ and historico_us/.'
    )
    parser.add_argument(
        '--output-name',
        dest='output_name',
        default=None,
        help='Base name for generated output files (default: Technical_Documentation).'
    )
    parser.add_argument(
        '--project-name',
        dest='project_name',
        default=None,
        help='Project name for titles and headers.'
    )
    return parser.parse_args()

def resolve_doc_dir(cli_doc_dir, skill_dir):
    if cli_doc_dir:
        return os.path.abspath(cli_doc_dir)

    env_dir = os.environ.get("DOCS_DIR")
    if env_dir and os.path.isdir(env_dir):
        return os.path.abspath(env_dir)

    cwd_candidate = os.path.abspath(os.path.join(os.getcwd(), 'documentacao'))
    if os.path.isdir(cwd_candidate):
        return cwd_candidate

    skill_doc_candidate = os.path.abspath(os.path.join(skill_dir, 'documentacao'))
    if os.path.isdir(skill_doc_candidate):
        return skill_doc_candidate

    parent_repo_candidate = os.path.abspath(os.path.join(skill_dir, '..', '..', '..', 'documentacao'))
    if os.path.isdir(parent_repo_candidate):
        return parent_repo_candidate

    sub_repo_candidate = os.path.abspath(os.path.join(skill_dir, '..', '..', 'documentacao'))
    if os.path.isdir(sub_repo_candidate):
        return sub_repo_candidate

    return skill_doc_candidate

def load_environment(skill_dir, doc_dir):
    candidates = [
        os.path.join(os.getcwd(), '.env'),
        os.path.join(skill_dir, '.env'),
        os.path.abspath(os.path.join(skill_dir, '..', '.env')),
        os.path.abspath(os.path.join(doc_dir, '..', '.env'))
    ]
    for env_path in candidates:
        if os.path.exists(env_path):
            load_env_file(env_path)
            break

def main():
    args = parse_args()
    should_send_email = args.send_email if args.email_flag is None else args.email_flag

    scripts_dir = os.path.dirname(os.path.abspath(__file__))
    skill_dir = os.path.abspath(os.path.join(scripts_dir, '..'))

    doc_dir = resolve_doc_dir(args.doc_dir, skill_dir)
    
    os.makedirs(os.path.join(doc_dir, 'topicos'), exist_ok=True)
    os.makedirs(os.path.join(doc_dir, 'historico_us'), exist_ok=True)

    load_environment(skill_dir, doc_dir)

    print("\n" + "="*70)
    print("  INITIALIZING DOCOPS ENGINE COMPILATION")
    print("="*70)
    print(f"• Documentation Directory: {doc_dir}")

    builder = BuildDocs(
        doc_dir=doc_dir,
        output_filename=args.output_name,
        project_name=args.project_name
    )
    master_md = builder.compile_modular_markdown(doc_dir)
    print(f"[OK] Compiled Markdown: {master_md}")

    docx_file = os.path.join(doc_dir, f"{builder.output_filename}.docx")
    builder.convert_md_to_docx(master_md, docx_file)

    if should_send_email:
        sender = SendDocs(doc_dir=doc_dir, project_name=builder.project_name)
        us_info = sender.get_latest_us_details()
        sender.send_documentation_update_email(docx_file, us_info)
    else:
        print("\n" + "="*70)
        print("[INFO] Documentation successfully compiled!")
        print("       Email dispatch skipped via flag (--no-email).")
        print("="*70 + "\n")

if __name__ == '__main__':
    main()
