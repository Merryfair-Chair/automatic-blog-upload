import os
import io
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/drive']
CREDENTIALS_PATH = os.getenv('GOOGLE_CREDENTIALS_PATH', 'C:/Users/wenxi.lee/seo-credentials.json')
FOLDER_NAME = 'Blog Post Material'

def get_drive_service():
    creds = service_account.Credentials.from_service_account_file(
        CREDENTIALS_PATH, scopes=SCOPES
    )
    return build('drive', 'v3', credentials=creds)

def find_folder(service, name):
    results = service.files().list(
        q=f"name='{name}' and mimeType='application/vnd.google-apps.folder' and trashed=false",
        fields="files(id, name)"
    ).execute()
    files = results.get('files', [])
    return files[0]['id'] if files else None

def upload_blog(title, content, faq_schema):
    service = get_drive_service()
    folder_id = find_folder(service, FOLDER_NAME)

    if not folder_id:
        raise Exception(f"Google Drive folder '{FOLDER_NAME}' not found. Please create it first.")

    full_content = f"{content}\n\n---\n\n## FAQ SCHEMA\n\n```html\n{faq_schema}\n```"
    file_content = full_content.encode('utf-8')

    safe_title = title.replace('/', '-').replace('\\', '-')
    file_metadata = {
        'name': f"{safe_title}.md",
        'parents': [folder_id],
        'mimeType': 'text/plain'
    }

    media = MediaIoBaseUpload(
        io.BytesIO(file_content),
        mimetype='text/plain',
        resumable=False
    )

    file = service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id, name, webViewLink'
    ).execute()

    return file.get('webViewLink'), file.get('name')
