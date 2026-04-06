import re
import base64
import requests
import os
import markdown as md_lib
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path(__file__).parent / ".env")

WP_URL       = os.getenv('WP_URL', 'https://www.merryfair.com')
WP_USERNAME  = os.getenv('WP_USERNAME', 'wenxi')
WP_APP_PASSWORD = os.getenv('WP_APP_PASSWORD', '')
SITE_URL     = 'https://www.merryfair.com'

# REST base for the Blogs custom post type
BLOG_POST_TYPE = 'cpt-blogs'


def get_headers():
    token = base64.b64encode(f"{WP_USERNAME}:{WP_APP_PASSWORD}".encode()).decode()
    return {'Authorization': f'Basic {token}', 'Content-Type': 'application/json'}


def apply_link_rules(tag):
    """Apply target and rel attributes to an <a> tag based on internal/external."""
    href = tag.get('href', '')
    if not href or href.startswith('#'):
        return
    if 'INTERNAL LINK' in href:
        tag['href'] = '#'
        tag['data-link-note'] = href
        tag['target'] = '_blank'
        tag['rel'] = 'noopener'
    elif 'merryfair.com' in href:
        tag['target'] = '_blank'
        tag['rel'] = 'noopener'
    else:
        tag['target'] = '_blank'
        tag['rel'] = 'noopener nofollow'



def markdown_to_wp_content(markdown_text):
    """Convert Markdown draft to clean HTML for WordPress."""
    # Replace image placeholders with HTML comments
    markdown_text = re.sub(r'\[IMAGE-FEATURED: ([^\]]+)\]', r'<!-- FEATURED IMAGE: \1 -->', markdown_text)
    markdown_text = re.sub(r'\[IMAGE-CONTENT: ([^\]]+)\]',  r'<!-- CONTENT IMAGE: \1 -->',  markdown_text)
    markdown_text = re.sub(r'\[IMAGE-DATA: ([^\]]+)\]',     r'<!-- MANUAL IMAGE: \1 -->',    markdown_text)

    # Remove [QUOTABLE] markers (keep text, drop marker)
    markdown_text = re.sub(r'\[QUOTABLE\]\s*', '', markdown_text)

    # Convert Markdown to clean HTML
    html = md_lib.markdown(markdown_text, extensions=['tables', 'fenced_code'])

    # Apply link rules to all <a> tags
    soup = BeautifulSoup(html, 'html.parser')
    for a in soup.find_all('a'):
        apply_link_rules(a)

    return str(soup)


def publish_draft(title, slug, markdown_content):
    """Publish blog post as Draft to WordPress Blogs post type."""
    wp_content = markdown_to_wp_content(markdown_content)

    post_data = {
        'title':   title,
        'slug':    slug,
        'content': wp_content,
        'status':  'draft',
    }

    r = requests.post(
        f"{WP_URL}/wp-json/wp/v2/{BLOG_POST_TYPE}",
        headers=get_headers(),
        json=post_data
    )

    if r.status_code not in (200, 201):
        raise Exception(f"WordPress publish failed: {r.status_code} — {r.text[:300]}")

    post = r.json()
    post_id = post.get('id')
    return post_id, post.get('link'), f"{WP_URL}/wp-admin/post.php?post={post_id}&action=edit"
