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
