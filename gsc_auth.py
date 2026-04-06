import os
import pickle
from pathlib import Path
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/webmasters.readonly']
CLIENT_SECRETS = str(Path.home() / 'oauth-client.json')
TOKEN_FILE = str(Path(__file__).parent / 'gsc-token.pickle')

def get_gsc_service():
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

    return build('searchconsole', 'v1', credentials=creds)

if __name__ == '__main__':
    service = get_gsc_service()
    sites = service.sites().list().execute()
    print("[OK] Authenticated with Google Search Console")
    print("[OK] Properties you have access to:")
    for site in sites.get('siteEntry', []):
        print(f"  - {site['siteUrl']} ({site['permissionLevel']})")
