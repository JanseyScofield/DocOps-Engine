---
name: docops-engine
description: DocOps Engine is a modular, AI-driven technical documentation system. Eliminates Git merge conflicts across concurrent feature branches using decoupled markdown modules (isolated user story logs in docs/user_stories/ and architectural topics in docs/topics/). Compiles both a single source of truth Markdown master document and styled Word (.docx) files, with automated stakeholder email alerts.
---

# ⚙️ DocOps Engine (Git-Optimized Documentation Skill)

> **🎯 Purpose:** Continuous, automated, and conflict-free technical documentation for modern software projects and AI coding agents.

---

## 🛠️ HOW TO ADAPT DOCOPS ENGINE FOR YOUR REPOSITORY (Setup Checklist)

When importing DocOps Engine into your project (inside `.ai/skills/docops-engine/`, `.cursor/skills/`, or agent system prompts), review the following:

1. **Skill Name & Frontmatter (`name`):**
   - Defined as `name: docops-engine`. Keep this identifier or adjust if your agent catalog uses a specific convention.
2. **Execution Path (Rule 3 & Step 5):**
   - Update the execution path to match where your scripts are located (e.g., `python scripts/main.py --no-email` or `python .ai/skills/docops-engine/scripts/main.py --no-email`).
3. **Architectural Topics (`docs/topics/`):**
   - In Section 1, customize the topic filenames to match your architecture (e.g., `1_architecture.md`, `2_database.md`, `3_setup.md`, `4_security.md`, `5_api_reference.md`).
4. **User Story Template (Section 3):**
   - Customize the tech-stack sections (`Backend Changes`, `Frontend Changes`, `Mobile Changes`, etc.) to match your actual repositories and directories.
5. **Agent Workflow & Triggers (Section 4):**
   - Define when DocOps Engine is triggered (e.g., upon story completion, after unit test approval, or before PR creation).

---

## 1. Modular Directory Structure in `docs/`

All documentation source files must reside in the `docs/` folder:

```text
<your-project-root>/
├── docs/
│   ├── Technical_Documentation.md        # Compiled Markdown master doc (Single Source of Truth for AI)
│   ├── Technical_Documentation.docx      # Compiled Microsoft Word master doc (Official Stakeholder Doc)
│   │
│   ├── topics/                           # Core Architectural Modules (Domain Isolated)
│   │   ├── 1_architecture.md             # Topic 1: System Overview, Layers & ADRs
│   │   ├── 2_database.md                 # Topic 2: Database Schema, Entities & Migrations
│   │   ├── 3_setup.md                    # Topic 3: Project Setup, Prerequisites & Execution
│   │   └── 4_skills.md                   # Topic 4: Tooling & AI Skills Catalog
│   │
│   └── user_stories/                     # Individual User Story / Bugfix Logs (ZERO Git Merge Conflicts)
│       ├── US-001_authentication.md
│       ├── US-002_data_pipeline.md
│       └── US-003_dashboard_analytics.md
```

---

## 2. Multi-Developer & Multi-Agent Git Conflict Prevention Rules

When two or more developers or AI agents work concurrently on parallel branches (e.g., `feature/US-010` and `feature/US-025`), enforce these rules:

### Rule 1: Isolated User Story Files (`docs/user_stories/`)
- Every feature, User Story, or bugfix must be documented in its **own standalone file** inside `docs/user_stories/US-XXX_slug.md`.
- **Why?** Git merges distinct new files automatically without collision. When concurrent branches are merged into `main` or `develop`, the merge completes with **ZERO merge conflicts**.

### Rule 2: Modular Topic Updates (`docs/topics/`)
- If a feature modifies the database (e.g., migrations/schemas), update only `docs/topics/2_database.md`.
- If a feature introduces an architectural pattern or ADR, update only `docs/topics/1_architecture.md`.
- Never modify unrelated topic files during a feature implementation.

### Rule 3: Single-Command Compilation & CLI Email Control
- DocOps Engine reads all modular files and generates the unified master documents (`.md` and `.docx`).
```bash
# Recommended default for development (Compiles without sending email):
python scripts/main.py --no-email

# Production / Stakeholder delivery (Compiles and sends email alerts):
python scripts/main.py --send-email
```

### Rule 4: Binary Word Document (.docx) Conflict Resolution
- If Git flags a binary conflict on `Technical_Documentation.docx` during a branch merge, accept either version and simply run `python scripts/main.py --no-email` post-merge to cleanly regenerate the binaries from the merged Markdown files.

---

## 3. Template for Individual User Story Files (`docs/user_stories/US-XXX.md`)

When creating a new file in `docs/user_stories/`, use this standardized schema:

```markdown
### US-XXX: [User Story Title or Bugfix Description]
- **Status:** Completed
- **Completion Date:** YYYY-MM-DD
- **Module:** [System Module Name]
- **Assignee:** [Developer Name or AI Agent]
- **Business Goal:** [Clear description of value delivered and problem solved]
- **Accepted Criteria:**
  - [x] Acceptance criteria 1...
  - [x] Acceptance criteria 2...
- **Backend Changes:**
  - `src/backend/...`: [Summary of endpoint, service, or handler changes]
- **Frontend Changes:**
  - `src/frontend/...`: [Summary of views, components, or state changes]
- **Tests & Validation:**
  - Unit test coverage threshold verified.
  - Integration tests and manual verification completed.
```

---

## 4. Execution Workflow for the Documenter Agent

1. **Trigger**: Triggered automatically upon completion or code-review approval of a user story or bugfix.
2. **Review Changes**: Inspect the Git diff and commit details of the implementation.
3. **Update Core Topics (if applicable)**: Edit relevant files in `docs/topics/` (e.g., database, architecture).
4. **Create US File**: Generate `docs/user_stories/US-XXX_[slug].md` using the template above.
5. **Recompile Master Documents**:
   ```bash
   python scripts/main.py --no-email
   ```
6. **Commit Suggestion**: Include documentation files in the feature commit (e.g., `docs: update modular documentation for US-XXX`).

---

## 5. Automated Email Notification Protocol & `.env`

Configuration is encapsulated in `.env` (copied from `.env.example`):
- **Developer Metadata**: `DEV_NAME` and `DEV_EMAIL`.
- **Stakeholder Recipients**: `DOC_EMAILS` (comma-separated list).
- **Brand Identity**: `BRAND_COLOR` (hex code used across Word headers and email styling).
- **SMTP Server**: `SMTP_HOST`, `SMTP_PORT`, `SMTP_USER`, `SMTP_PASSWORD`.
- **Email Body**: Responsive HTML layout located in `scripts/templates/email_notification.html` with US details, delivery badges, and attached `.docx` file.
