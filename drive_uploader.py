import os
import io
import pickle
import re
import markdown as md_lib
from pathlib import Path
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/drive']
CLIENT_SECRETS = 'C:/Users/wenxi.lee/oauth-client.json'
TOKEN_FILE = str(Path(__file__).parent / 'drive-token.pickle')
FOLDER_NAME = 'Blog Post Material'


def get_drive_service():
    creds = None
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'rb') as f:
            creds = pickle.load(f)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_FILE, 'wb') as f:
            pickle.dump(creds, f)

    return build('drive', 'v3', credentials=creds)


def find_folder(service, name):
    results = service.files().list(
        q=f"name='{name}' and mimeType='application/vnd.google-apps.folder' and trashed=false",
        fields="files(id, name)"
    ).execute()
    files = results.get('files', [])
    return files[0]['id'] if files else None


def markdown_to_html(markdown_text, faq_schema):
    """Convert Markdown + FAQ schema to clean HTML for Google Docs import."""
    # Clean up image placeholders for readability
    markdown_text = re.sub(r'\[IMAGE-FEATURED: ([^\]]+)\]', r'\n\n**[FEATURED IMAGE: \1]**\n\n', markdown_text)
    markdown_text = re.sub(r'\[IMAGE-CONTENT: ([^\]]+)\]',  r'\n\n**[CONTENT IMAGE: \1]**\n\n',  markdown_text)
    markdown_text = re.sub(r'\[IMAGE-DATA: ([^\]]+)\]',     r'\n\n**[MANUAL IMAGE: \1]**\n\n',    markdown_text)
    markdown_text = re.sub(r'\[QUOTABLE\]\s*', '', markdown_text)

    # Convert Markdown to HTML
    body_html = md_lib.markdown(markdown_text, extensions=['tables', 'fenced_code'])

    # Append FAQ schema as readable code block
    faq_html = ''
    if faq_schema:
        faq_html = (
            '<hr>'
            '<h2>FAQ SCHEMA (Custom HTML Block)</h2>'
            f'<pre><code>{faq_schema}</code></pre>'
        )

    # Wrap in clean HTML document
    html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
  body {{ font-family: Arial, sans-serif; font-size: 11pt; line-height: 1.6; max-width: 800px; margin: 40px auto; }}
  h1 {{ font-size: 20pt; }} h2 {{ font-size: 16pt; }} h3 {{ font-size: 13pt; }}
  table {{ border-collapse: collapse; width: 100%; }}
  th, td {{ border: 1px solid #ccc; padding: 8px; text-align: left; }}
  pre {{ background: #f4f4f4; padding: 12px; font-size: 9pt; white-space: pre-wrap; }}
  code {{ background: #f4f4f4; padding: 2px 4px; }}
</style>
</head>
<body>
{body_html}
{faq_html}
</body>
</html>"""
    return html


def upload_blog(title, content, faq_schema):
    service = get_drive_service()
    folder_id = find_folder(service, FOLDER_NAME)

    if not folder_id:
        raise Exception(f"Google Drive folder '{FOLDER_NAME}' not found.")

    # Convert Markdown to HTML
    html_content = markdown_to_html(content, faq_schema)
    file_bytes = html_content.encode('utf-8')

    safe_title = re.sub(r'[<>:"/\\|?*]', '-', title)

    # Upload as HTML and convert to Google Doc automatically
    file_metadata = {
        'name': safe_title,
        'parents': [folder_id],
        'mimeType': 'application/vnd.google-apps.document'  # auto-converts to Google Doc
    }

    media = MediaIoBaseUpload(
        io.BytesIO(file_bytes),
        mimetype='text/html',
        resumable=False
    )

    file = service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id, name, webViewLink'
    ).execute()

    return file.get('webViewLink'), file.get('name')


if __name__ == '__main__':
    service = get_drive_service()
    folder_id = find_folder(service, FOLDER_NAME)
    if folder_id:
        print(f"[OK] Connected to your Google Drive")
        print(f"[OK] Found folder: '{FOLDER_NAME}' (ID: {folder_id})")
    else:
        print(f"[ERROR] Folder '{FOLDER_NAME}' not found in your Drive")
