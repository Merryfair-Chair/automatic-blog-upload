import os
import io
import pickle
from pathlib import Path
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = [
    'https://www.googleapis.com/auth/drive',
]
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


if __name__ == '__main__':
    service = get_drive_service()
    folder_id = find_folder(service, FOLDER_NAME)
    if folder_id:
        print(f"[OK] Connected to your Google Drive")
        print(f"[OK] Found folder: '{FOLDER_NAME}' (ID: {folder_id})")
    else:
        print(f"[ERROR] Folder '{FOLDER_NAME}' not found in your Drive")
