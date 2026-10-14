import datetime
import smtplib
import os
import glob
import re
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from email_template import EmailTemplate

class SendDocs:
    def __init__(self, doc_dir, project_name=None, brand_color=None):
        self.doc_dir = os.path.abspath(doc_dir)
        self.project_name = project_name or os.environ.get("PROJECT_NAME", "Project")
        self.brand_color = brand_color or os.environ.get("BRAND_COLOR", "#005BAA")
        
        self.dev_name = os.environ.get("DEV_NAME", "Lead Developer")
        self.dev_email = os.environ.get("DEV_EMAIL", os.environ.get("SMTP_USER", "developer@example.com"))
        self.us_info = self.get_latest_us_details()

    def get_latest_us_details(self):
        us_dir = os.path.join(self.doc_dir, 'user_stories') if os.path.exists(os.path.join(self.doc_dir, 'user_stories')) else os.path.join(self.doc_dir, 'historico_us')
        
        us_files = sorted(glob.glob(os.path.join(us_dir, 'US-*.md')), key=os.path.getmtime, reverse=True)
        if us_files:
            latest_file = us_files[0]
            with open(latest_file, 'r', encoding='utf-8') as f:
                content = f.read().strip()
                
            us_id_match = re.search(r'###\s*(US-\d+|US-[A-Za-z0-9\-]+):\s*(.*)', content)
            modulo_match = re.search(r'-\s*\*\*(?:Module|Módulo):\*\*\s*(.*)', content, re.IGNORECASE)
            objetivo_match = re.search(r'-\s*\*\*(?:Business Goal|Objetivo de Negócio):\*\*\s*(.*)', content, re.IGNORECASE)
            
            us_id = us_id_match.group(1) if us_id_match else "Recent US"
            titulo = us_id_match.group(2) if us_id_match else os.path.basename(latest_file)
            modulo = modulo_match.group(1) if modulo_match else "General"
            objetivo = objetivo_match.group(1) if objetivo_match else "System functionality update."
            
            return {
                "id": us_id,
                "titulo": titulo,
                "modulo": modulo,
                "objetivo": objetivo,
                "arquivo": os.path.basename(latest_file),
                "conteudo": content
            }

        return {
            "id": "General Update",
            "titulo": f"Technical Documentation Sync - {self.project_name}",
            "modulo": "Governance & Architecture",
            "objetivo": "Continuous update of architectural guidelines and specifications.",
            "arquivo": "Technical_Documentation.md",
            "conteudo": ""
        }

    def send_documentation_update_email(self, docx_path, us_info=None):
        us_info = us_info or self.us_info
        dev_name = self.dev_name
        dev_email = self.dev_email
        project_name = self.project_name
        brand_color = self.brand_color
        docx_filename = os.path.basename(docx_path) if docx_path else "Technical_Documentation.docx"

        raw_recipients = os.environ.get("DOC_EMAILS", os.environ.get("SAET_DOC_EMAILS", "")).split(",")
        recipients = list(dict.fromkeys([r.strip() for r in raw_recipients if r.strip()]))
        if not recipients:
            recipients = [dev_email]

        now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        subject = f"Documentation Update - {project_name} - {us_info['id']}"

        template_builder = EmailTemplate(
            project_name=project_name,
            brand_color=brand_color,
            us_info=us_info,
            dev_name=dev_name,
            dev_email=dev_email,
            date_time=now_str,
            docx_filename=docx_filename
        )
        text_content, html_content = template_builder.render()

        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = f"{dev_name} <{dev_email}>"
        msg['To'] = ", ".join(recipients)

        msg.attach(MIMEText(text_content, 'plain', 'utf-8'))
        msg.attach(MIMEText(html_content, 'html', 'utf-8'))

        if docx_path and os.path.exists(docx_path):
            try:
                with open(docx_path, 'rb') as attachment:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f'attachment; filename="{docx_filename}"')
                msg.attach(part)
            except Exception as e:
                print(f"[EMAIL] Warning attaching DOCX document: {e}")

        smtp_host = os.environ.get("SMTP_HOST", "localhost")
        smtp_port = int(os.environ.get("SMTP_PORT", 25))
        smtp_user = os.environ.get("SMTP_USER", None)
        smtp_pass = os.environ.get("SMTP_PASSWORD", None)

        print("\n" + "="*70)
        print("[EMAIL] DISPATCHING DOCUMENTATION NOTIFICATION")
        print("="*70)
        print(f"• Sender: {dev_name} <{dev_email}>")
        print(f"• Recipients: {', '.join(recipients)}")
        print(f"• Subject: {msg['Subject']}")
        print(f"• Delivery/US: {us_info['id']} - {us_info['titulo']}")
        print(f"• Date/Time: {now_str}")
        print("="*70)

        try:
            if smtp_user and smtp_pass:
                with smtplib.SMTP(smtp_host, smtp_port, timeout=10) as server:
                    server.starttls()
                    server.login(smtp_user, smtp_pass)
                    server.sendmail(dev_email, recipients, msg.as_string())
                print("[OK] Email successfully sent via SMTP server!")
            else:
                with smtplib.SMTP(smtp_host, smtp_port, timeout=5) as server:
                    server.sendmail(dev_email, recipients, msg.as_string())
                print("[OK] Email successfully sent via local SMTP relay!")
        except Exception as e:
            print(f"[SMTP ERROR] Failed to send email: {e}")
            print(f"             Check SMTP_HOST ({smtp_host}), port ({smtp_port}), and credentials in .env.")
        print("="*70 + "\n")
