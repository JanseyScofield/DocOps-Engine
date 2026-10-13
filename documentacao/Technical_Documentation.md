# Technical & Architectural Documentation - Project

> *Note: This document is automatically and continuously compiled from modular documentation source files.*

---

## Topic 1: System Architecture

### 1.1 Overview and Architectural Patterns
This document outlines the software architecture decisions adopted in this project. The system follows a modern decoupled architecture that promotes maintainability, horizontal scalability, and continuous evolution.

- **Design Pattern:** Clean Architecture / Vertical Slice Architecture.
- **Communication:** RESTful APIs / Asynchronous Event-Driven Messaging.
- **Resilience & Fault Tolerance:** Retry policies, Circuit Breakers, and structured logging.

### 1.2 Architecture Decision Records (ADRs)
Structural decisions and modifications are tracked through Architecture Decision Records (ADRs):

| ID | Date | Title | Status | Primary Impact |
|---|---|---|---|---|
| ADR-001 | 2026-01-10 | Modular Architecture Adoption | Accepted | Eliminates tight domain coupling across services. |
| ADR-002 | 2026-02-15 | Automated Incremental Documentation | Accepted | Prevents specification and code divergence. |
| ADR-003 | 2026-03-20 | Automated Stakeholder Notifications | Accepted | Provides immediate visibility into delivered features. |

---

## Topic 2: Database and Data Models

### 2.1 DBMS Overview
The persistence layer is designed to ensure relational integrity, performance, and transactional consistency.

- **Primary DBMS:** PostgreSQL / SQL Server / SQLite.
- **ORM / Data Access:** Entity Framework Core / Dapper / SQLAlchemy.
- **Migration Strategy:** Code-first migrations managed through version control.

### 2.2 Core Entities and Tables
The foundational database entities are described below:

| Table | Description | Key Indexes |
|---|---|---|
| `Users` | Authentication credentials, user profiles, and roles. | `PK_Users_Id`, `UK_Users_Email` |
| `AuditLogs` | Audit trail of security events and operational updates. | `PK_Audit_Id`, `IX_Audit_CreatedAt` |
| `Configurations` | Dynamic system settings and feature toggles. | `PK_Config_Key` |

### 2.3 Migration History
Record every database migration upon release:
- `20260110_InitialMigration`: Baseline schema creation.
- `20260215_AddAuditLogs`: Audit tracking tables and indexes.

---

## Topic 3: Project Setup and Environment Configuration

### 3.1 Prerequisites
Before setting up the project locally, ensure you have the following installed:

- **Python:** Version 3.10 or higher.
- **Git:** Installed and configured with your user credentials.
- **IDE / Editor:** Visual Studio Code, Cursor, or your preferred IDE.

### 3.2 Step-by-Step Initial Setup

1. **Clone the Repository:**
   ```bash
   git clone <REPOSITORY_URL>
   cd my-project
   ```

2. **Create and Activate a Virtual Environment:**
   ```bash
   # Windows PowerShell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1

   # Linux / macOS / Git Bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables:**
   Copy `.env.example` to `.env` and fill in the values according to your development environment.

---

## Topic 4: AI Skills & Tooling Catalog

### 4.1 Overview of AI Skills
This repository uses standardized AI skills to streamline Spec-Driven Development:

- **documentacao:** Automated compilation of consolidated documentation (.md and .docx) with Git conflict elimination and stakeholder email notifications.
- **code-review:** Static code analysis checklists and quality gate verification.
- **commits:** Semantic commit standards adhering to Conventional Commits.

### 4.2 Running the Documentation Skill
To compile and generate consolidated project documentation:

```bash
# Compile locally without sending email notifications:
python scripts/main.py --no-email

# Compile and send Word (.docx) report to stakeholders:
python scripts/main.py --send-email
```

---

## Topic 5: User Stories & Feature History

### 5.1 Traceability Matrix

| US ID | Title / Feature | Module | Status | Completion Date |
|---|---|---|---|---|
| US-001 | Initial Setup and Modular Documentation Architecture | Governance & Automation | Completed | 2026-10-13 |

### 5.2 Detailed History by User Story / Bug Fix

### US-001: Initial Setup and Modular Documentation Architecture
- **Status:** Completed
- **Completion Date:** 2026-10-13
- **Module:** Governance & Automation
- **Assignee:** Developer / Documenter Agent
- **Business Goal:** Establish a decoupled modular documentation architecture to eliminate Git merge conflicts during concurrent multi-developer branches.
- **Accepted Criteria:**
  - [x] Create isolated topic modules inside `topicos/`.
  - [x] Isolate individual user story notes into standalone markdown files inside `historico_us/`.
  - [x] Python compiler script assembling all files into a consolidated Markdown master document.
  - [x] Automatic conversion into professional Microsoft Word (.docx) with brand headers and styled tables.
  - [x] Configurable SMTP email notifications with official document attachments for stakeholders.
- **Backend / Script Changes:**
  - `scripts/build_docs.py`: Modular Markdown assembler and `.docx` converter.
  - `scripts/send_docs.py`: SMTP notification handler with email attachment delivery.
  - `scripts/email_template.py`: Decoupled email renderer supporting HTML and plain-text.
  - `scripts/main.py`: CLI entrypoint with `--no-email` and `--send-email` options.
- **Templates & Documentation Changes:**
  - Topic blueprints in `documentacao/topicos/` and sample story in `documentacao/historico_us/`.
- **Tests & Validation:**
  - Validated on Python 3.12 virtual environment (`.venv`).
  - Successfully generated consolidated `.md` and `.docx` documents.
