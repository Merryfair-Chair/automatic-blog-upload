import requests
import base64

WP_URL = "https://www.merryfair.com"
USERNAME = "wenxi"
APP_PASSWORD = "ELJ8 KvK5 MnsD z6hW FtPN 60ax"

token = base64.b64encode(f"{USERNAME}:{APP_PASSWORD}".encode()).decode()
headers = {"Authorization": f"Basic {token}"}

# Test 1: Auth
r = requests.get(f"{WP_URL}/wp-json/wp/v2/users/me", headers=headers)
user = r.json()
print(f"[OK] Authenticated as: {user.get('name')} (ID: {user.get('id')})")

# Test 2: Fetch recent posts
r = requests.get(f"{WP_URL}/wp-json/wp/v2/posts?per_page=3", headers=headers)
posts = r.json()
print(f"[OK] Recent posts:")
for p in posts:
    print(f"  - [{p['status']}] {p['title']['rendered']}")

# Test 3: Fetch categories
r = requests.get(f"{WP_URL}/wp-json/wp/v2/categories?per_page=5", headers=headers)
cats = r.json()
print(f"[OK] Categories: {[c['name'] for c in cats]}")
