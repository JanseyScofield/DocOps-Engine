import os

class EmailTemplate:
    def __init__(self, project_name, brand_color, us_info, dev_name, dev_email, date_time, docx_filename=None):
        self.project_name = project_name
        self.brand_color = brand_color
        self.us_info = us_info or {}
        self.dev_name = dev_name
        self.dev_email = dev_email
        self.date_time = date_time
        self.docx_filename = docx_filename or "Technical_Documentation.docx"

    def render_text(self):
        us_id = self.us_info.get('id', 'Update')
        titulo = self.us_info.get('titulo', 'Documentation Sync')
        modulo = self.us_info.get('modulo', 'General')
        objetivo = self.us_info.get('objetivo', 'Technical system update.')

        return (
            f"Hello,\n\n"
            f"The technical and architectural documentation for project '{self.project_name}' has been successfully updated!\n\n"
            f"--------------------------------------------------\n"
            f"USER STORY / UPDATE DETAILS:\n"
            f"--------------------------------------------------\n"
            f"• Identifier: {us_id}\n"
            f"• Title: {titulo}\n"
            f"• Module: {modulo}\n"
            f"• Business Goal: {objetivo}\n"
            f"• Assignee: {self.dev_name} ({self.dev_email})\n"
            f"• Date: {self.date_time}\n\n"
            f"The official Word document ({self.docx_filename}) is attached to this message.\n\n"
            f"Best regards,\n"
            f"Engineering Team - {self.project_name}"
        )

    def render_html(self, template_path=None):
        if template_path is None:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            template_path = os.path.join(current_dir, 'templates', 'email_notification.html')

        replacements = {
            "{{PROJECT_NAME}}": str(self.project_name),
            "{{BRAND_COLOR}}": str(self.brand_color),
            "{{US_ID}}": str(self.us_info.get('id', 'Update')),
            "{{US_TITLE}}": str(self.us_info.get('titulo', 'Documentation Sync')),
            "{{US_MODULE}}": str(self.us_info.get('modulo', 'General')),
            "{{US_GOAL}}": str(self.us_info.get('objetivo', 'Technical system update.')),
            "{{DEV_NAME}}": str(self.dev_name),
            "{{DEV_EMAIL}}": str(self.dev_email),
            "{{DATE_TIME}}": str(self.date_time),
            "{{DOCX_FILENAME}}": str(self.docx_filename)
        }

        if os.path.exists(template_path):
            with open(template_path, 'r', encoding='utf-8') as f:
                html = f.read()
            for placeholder, value in replacements.items():
                html = html.replace(placeholder, value)
            return html

        return self._render_inline_fallback(replacements)

    def _render_inline_fallback(self, replacements):
        return f"""<!DOCTYPE html>
<html>
<head><meta charset="utf-8"></head>
<body style="font-family: Arial, sans-serif; padding: 20px;">
    <h2>Technical Documentation Update - {replacements['{{PROJECT_NAME}}']}</h2>
    <p><strong>Delivery:</strong> {replacements['{{US_ID}}']} - {replacements['{{US_TITLE}}']}</p>
    <p><strong>Module:</strong> {replacements['{{US_MODULE}}']}</p>
    <p><strong>Goal:</strong> {replacements['{{US_GOAL}}']}</p>
    <p><strong>Assignee:</strong> {replacements['{{DEV_NAME}}']} ({replacements['{{DEV_EMAIL}}']})</p>
    <p><strong>Date:</strong> {replacements['{{DATE_TIME}}']}</p>
</body>
</html>"""

    def render(self, template_path=None):
        return self.render_text(), self.render_html(template_path)
