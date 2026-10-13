# ⚙️ DocOps Engine

<p align="center">
  <a href="README.md"><b>🇬🇧 English</b></a> •
  <a href="README.pt-BR.md">🇧🇷 Português</a>
</p>

---

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Zero Git Conflicts](https://img.shields.io/badge/Git-Zero%20Merge%20Conflicts-brightgreen.svg)]()
[![Documentation](https://img.shields.io/badge/Docs-Markdown%20%26%20DOCX-orange.svg)]()

> **DocOps Engine:** A conflict-free, modular, and automated technical documentation engine designed for agile engineering teams and AI coding agents.

---

## 🎯 Why DocOps Engine? (The Problem It Solves)

When multiple developers or autonomous AI coding agents work concurrently on separate Git branches (e.g., `feature/US-010` and `feature/US-025`), centralized documentation files inevitably suffer from **frequent and painful Git merge conflicts**.

**DocOps Engine** implements a **Decoupled Modular Documentation Architecture**:

1. **Isolated User Story Files (`historico_us/`)**: Every feature, user story, or bugfix is documented in its own standalone file (`US-XXX_slug.md`). Because Git merges distinct new files automatically without collisions, combining parallel branches results in **ZERO merge conflicts**.
2. **Modular Architecture Topics (`topicos/`)**: Core architectural domains (Database, Infrastructure, System Overview, AI Skills) are isolated into independent topic files.
3. **Automated Single-Step Compiler (`scripts/main.py`)**: Assembles all topics and user stories, creates an automatic traceability matrix, and compiles both a consolidated Markdown file (Single Source of Truth for AI) and an official Microsoft Word (`.docx`) document with corporate styling and zebra-striped tables.
4. **Automated Stakeholder Notifications (`scripts/send_docs.py`)**: Optionally sends responsive HTML email notifications via SMTP with the latest delivery summary and the generated `.docx` file attached.

---

## 📁 Repository Structure

```text
docops-engine/
├── .env.example                     # Environment configuration template
├── .gitignore                       # Git ignore rules (.env, .venv, etc.)
├── LICENSE                          # MIT License
├── README.md                        # English documentation (GitHub Default)
├── README.pt-BR.md                  # Portuguese documentation
├── requirements.txt                 # Python dependencies (python-docx)
├── SKILL.md                         # Formal AI Agent Skill definition
│
├── scripts/                         # Python automation engine
│   ├── build_docs.py                # Modular compiler (Markdown -> Styled DOCX)
│   ├── email_template.py            # Email content renderer (HTML & Plain Text)
│   ├── load_env.py                  # Zero-dependency .env reader
│   ├── main.py                      # CLI entrypoint and orchestrator
│   ├── send_docs.py                 # SMTP notification service with attachment
│   └── templates/                   # Decoupled visual templates
│       └── email_notification.html  # Responsive HTML template with placeholders
│
└── documentacao/                    # Project documentation workspace
    ├── Technical_Documentation.md   # [Generated] Consolidated Markdown master doc
    ├── Technical_Documentation.docx # [Generated] Styled Microsoft Word master doc
    │
    ├── topicos/                     # Isolated architectural topics
    │   ├── 1_architecture.md        # Architecture overview & ADRs
    │   ├── 2_database.md            # Database schema, tables & migrations
    │   ├── 3_setup.md               # Setup, prerequisites & run instructions
    │   └── 4_skills.md              # AI skills & tooling catalog
    │
    └── historico_us/                # Individual user story logs (1 file per US)
        └── US-001_initial_setup.md
```

---

## 🚀 Getting Started with Python Virtual Environment (`venv`)

No Docker required. The skill runs natively using your system's Python interpreter.

### 1. Prerequisites
- **Python 3.10+** installed.
- Git installed.

### 2. Setup Guide

#### Step 2.1 — Create the Virtual Environment
Open your terminal inside the repository folder:

```bash
# Windows (PowerShell or CMD)
python -m venv .venv

# Linux / macOS
python3 -m venv .venv
```

#### Step 2.2 — Activate the Virtual Environment

- **Windows (PowerShell):**
  ```powershell
  .\.venv\Scripts\Activate.ps1
  ```
  *(If script execution is blocked on Windows, run once: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`)*

- **Windows (CMD):**
  ```cmd
  .\.venv\Scripts\activate.bat
  ```

- **Linux / macOS:**
  ```bash
  source .venv/bin/activate
  ```

#### Step 2.3 — Install Dependencies
With the virtual environment active:
```bash
pip install -r requirements.txt
```

---

## ⚙️ Environment Variables Configuration (`.env`)

Copy `.env.example` to create your local `.env`:

```bash
# Windows (PowerShell)
Copy-Item .env.example .env

# Linux / macOS / Bash
cp .env.example .env
```

Open `.env` and fill in your settings:

```ini
# Project Identification
PROJECT_NAME="My Project"
DOC_TITLE="Technical & Architectural Documentation"
OUTPUT_FILENAME="Technical_Documentation"
BRAND_COLOR="#005BAA"

# Developer Metadata
DEV_NAME="Your Full Name"
DEV_EMAIL="your.email@company.com"

# SMTP Notification Server
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your.email@company.com
SMTP_PASSWORD=your_app_password

# Stakeholders receiving automated doc updates
DOC_EMAILS=tech.lead@company.com,product.owner@company.com
```

> ⚠️ **Security Tip:** The `.env` file should never be committed to Git. It is already included in `.gitignore`. When using Gmail, generate an **App Password** from your Google Account settings.

---

## 💻 Usage & CLI Commands

With `.venv` activated:

### 1. Compile Only (No email sent) — Recommended for Local Dev
Use this during routine development or internal documentation refactoring:
```bash
python scripts/main.py --no-email
```
or:
```bash
python scripts/main.py --skip-email
```

### 2. Compile and Notify Stakeholders via Email
Compiles the documents and automatically dispatches an HTML email report with the `.docx` attached:
```bash
python scripts/main.py --send-email
```

### 3. Optional CLI Flags
- `--doc-dir <path>`: Custom path to a `documentacao/` folder containing `topicos/` and `historico_us/`.
- `--output-name <name>`: Custom base name for generated files (e.g. `--output-name Core_Architecture`).
- `--project-name <name>`: Custom project title for headers and email templates.

Example:
```bash
python scripts/main.py --doc-dir "./custom-docs" --output-name "SystemSpec" --no-email
```

---

## 🎨 Complete Customization Guide (Colors, Messages & Branding)

> 💡 **100% Flexible & Brand-Agnostic:** This skill is engineered to adapt seamlessly to any company or personal project visual identity. You can customize corporate brand colors, email designs, document headers, and output naming in seconds.

### 1. How to Change Your Brand Color (`BRAND_COLOR`)
The project uses a single central color variable that automatically styles **both the generated Microsoft Word document (`.docx`) and the HTML notification email**.

In your `.env` file, change `BRAND_COLOR`:
```ini
# Example: Corporate Blue (Default)
BRAND_COLOR="#005BAA"

# Other popular examples:
# BRAND_COLOR="#10B981"  # Modern Green / Fintech
# BRAND_COLOR="#6366F1"  # Tech Indigo / Purple
# BRAND_COLOR="#FF6B00"  # Vibrant Orange
# BRAND_COLOR="#0F172A"  # Elegant Slate / Dark
```

**Where the color is automatically applied:**
- **In Word Documents (`.docx`):** Main headers (`# H1` & `## H2`), secondary headers (`### H3`), and colored table header row backgrounds.
- **In HTML Emails:** Header banner, US badges, notice callout borders, and accent highlights.

---

### 2. How to Customize Email Messages & HTML Layout
The email presentation is completely decoupled from the Python code and lives in:
📂 `scripts/templates/email_notification.html`

You can open this file in any IDE and edit it with full HTML/CSS syntax highlighting.

#### 🏷️ Available Dynamic Placeholders:
The script automatically replaces the following template tags:

| Placeholder | Description | Example Replaced Value |
|---|---|---|
| `{{PROJECT_NAME}}` | Configured project title | `"Customer Portal"` |
| `{{BRAND_COLOR}}` | Hex color code | `"#005BAA"` |
| `{{US_ID}}` | Delivery / US identifier | `"US-010"` |
| `{{US_TITLE}}` | Feature title | `"Payment Gateway Integration"` |
| `{{US_MODULE}}` | Affected module | `"Billing"` |
| `{{US_GOAL}}` | Business objective & delivered value | `"Enable Pix and Credit Card payments"` |
| `{{DEV_NAME}}` | Assignee / Developer name | `"Jansey Scofield"` |
| `{{DEV_EMAIL}}` | Contact email | `"dev@company.com"` |
| `{{DATE_TIME}}` | Compilation timestamp | `"2026-10-13 14:00"` |
| `{{DOCX_FILENAME}}` | Attached Word file name | `"Technical_Documentation.docx"` |

#### ✍️ How to Add Your Company Logo:
In `scripts/templates/email_notification.html`, locate the `.header` block and insert an image tag:
```html
<div class="header">
    <img src="https://your-company.com/logo.png" alt="Logo" style="max-height: 40px; margin-bottom: 10px;" />
    <h1>Technical Documentation Update</h1>
    <p>{{PROJECT_NAME}}</p>
</div>
```

#### ✉️ How to Customize the Plain-Text Fallback Message:
For text-only email clients, customize the string in the `render_text()` method inside:
📂 `scripts/email_template.py`

---

### 3. Customizing Project Title and Output File Names
Configure custom naming either via `.env` or terminal flags:

- **Via `.env`:**
  ```ini
  PROJECT_NAME="Core Banking API"
  DOC_TITLE="Architecture & Engineering Manual"
  OUTPUT_FILENAME="Architecture_Manual"
  ```
- **Via CLI Arguments:**
  ```bash
  python scripts/main.py --project-name "Banking API" --output-name "Architecture_Manual" --no-email
  ```
  This creates `Architecture_Manual.md` and `Architecture_Manual.docx` with custom headers.

---

### 4. Customizing Architectural Topic Structure
You can structure your documentation to match any domain. Simply add or rename files in `documentacao/topicos/`:
- `1_overview.md`
- `2_architecture_decisions.md`
- `3_data_models.md`
- `4_security_compliance.md`
- `5_rest_apis.md`

The compiler automatically scans all files starting with digits (`[0-9]_*.md`) and orders them sequentially.

---

## 📝 Documenting a New User Story (`historico_us/`)

For each completed feature or bugfix, create a file named `US-XXX_slug.md` inside `documentacao/historico_us/`:

```markdown
### US-002: JWT Authentication Implementation
- **Status:** Completed
- **Completion Date:** 2026-10-13
- **Module:** Security / Auth
- **Assignee:** Developer / Documenter Agent
- **Business Goal:** Secure API endpoints through signed cryptographic tokens and automated refresh tokens.
- **Accepted Criteria:**
  - [x] Login endpoint `/api/v1/auth/login` validating credentials.
  - [x] Authorization middleware enforcing claim validation.
- **Backend Changes:**
  - `src/Security/JwtTokenService.cs`: Token generation and signing.
- **Frontend Changes:**
  - `src/services/api.ts`: Axios interceptor injecting Bearer tokens.
- **Tests & Validation:**
  - Unit test coverage reached 92%.
```

Running `python scripts/main.py` automatically updates the traceability table and re-compiles both master documents!

---

## 🤖 Reusing as an AI Agent Skill

This skill is fully portable and compatible with modern AI development environments, such as **Google Antigravity**, **Cursor AI**, **Claude Code**, **GitHub Copilot**, and **Windsurf**:

1. **Drop-in Installation:**
   Copy the `scripts/` folder, `documentacao/` folder, and `SKILL.md` into your target repository's skills directory (e.g., `.ai/skills/documentacao/` or `.cursor/skills/documentacao/`).

2. **What to Customize in `SKILL.md` for Your Project (Setup Checklist):**
   The `SKILL.md` file comes with a dedicated top section (`HOW TO ADAPT THIS SKILL FOR YOUR REPOSITORY`). Review these items:
   - **Script Execution Path (Rule 3 & Step 5):** If scripts are placed in a subfolder such as `.ai/skills/documentacao/scripts/`, update the command in `SKILL.md` accordingly (e.g., `python .ai/skills/documentacao/scripts/main.py --no-email`).
   - **Architectural Topics (Section 1):** Tailor the topic files in `documentacao/topicos/` to match your system domains (e.g., `1_architecture.md`, `2_database.md`, `3_apis.md`).
   - **US Template (Section 3):** Customize directory paths under code changes (`Backend Changes`, `Frontend Changes`, etc.) to match your actual repo structure.
   - **Execution Triggers (Section 4):** Define whether docs should compile per approved user story or right before opening a Pull Request.

3. **Autonomous Execution by AI Agents:**
   AI agents will automatically follow `SKILL.md` guidelines:
   - Create isolated files in `documentacao/historico_us/US-XXX.md`.
   - Never overwrite existing US files from other branches (guaranteeing zero merge conflicts in Git).
   - Run `python scripts/main.py --no-email` after passing tests to maintain up-to-date master documentation.

---

## 📄 License

Distributed under the **MIT License**. See [LICENSE](LICENSE) for details.
