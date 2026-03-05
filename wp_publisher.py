import re
import base64
import requests
import os
import markdown as md_lib

WP_URL = os.getenv('WP_URL', 'https://www.merryfair.com')
WP_USERNAME = os.getenv('WP_USERNAME', 'wenxi')
WP_APP_PASSWORD = os.getenv('WP_APP_PASSWORD', '')
SITE_URL = 'https://www.merryfair.com'

def get_headers():
    token = base64.b64encode(f"{WP_USERNAME}:{WP_APP_PASSWORD}".encode()).decode()
    return {
        'Authorization': f'Basic {token}',
        'Content-Type': 'application/json'
    }

def apply_link_rules(html):
    """Apply internal/external link target and rel attributes."""
    def replace_link(m):
        href = m.group(1)
        inner = m.group(2)
        # Internal link placeholder (unresolved)
        if 'INTERNAL LINK' in href:
            return f'<a href="#" data-link-note="{href}" target="_blank" rel="noopener">{inner}</a>'
        # Internal link (merryfair.com)
        elif 'merryfair.com' in href:
            return f'<a href="{href}" target="_blank" rel="noopener">{inner}</a>'
        # External link
        else:
            return f'<a href="{href}" target="_blank" rel="noopener nofollow">{inner}</a>'

    return re.sub(r'<a href="([^"]*)"[^>]*>(.*?)</a>', replace_link, html)

def wrap_gutenberg_blocks(html):
    """Wrap HTML content in proper Gutenberg block comments."""
    blocks = []
    # Split content into lines for block-level processing
    # Use wp:freeform (classic block) for complex content — clean and reliable
    blocks.append('<!-- wp:freeform -->')
    blocks.append(html)
    blocks.append('<!-- /wp:freeform -->')
    return '\n'.join(blocks)

def faq_schema_block(schema_html):
    """Wrap FAQ schema in a Custom HTML block."""
    return f'<!-- wp:html -->\n{schema_html}\n<!-- /wp:html -->'

def markdown_to_wp_content(markdown_text, faq_schema):
    """Convert markdown draft to WordPress block editor content."""
    # Handle image placeholders — convert to comments for editor review
    markdown_text = re.sub(
        r'\[IMAGE-FEATURED: ([^\]]+)\]',
        r'<!-- FEATURED IMAGE: \1 -->',
        markdown_text
    )
    markdown_text = re.sub(
        r'\[IMAGE-CONTENT: ([^\]]+)\]',
        r'<!-- CONTENT IMAGE: \1 -->',
        markdown_text
    )
    markdown_text = re.sub(
        r'\[IMAGE-DATA: ([^\]]+)\]',
        r'<!-- MANUAL IMAGE NEEDED: \1 -->',
        markdown_text
    )

    # Convert Markdown to HTML
    html = md_lib.markdown(
        markdown_text,
        extensions=['tables', 'fenced_code', 'nl2br']
    )

    # Apply link rules
    html = apply_link_rules(html)

    # Wrap in Gutenberg blocks
    content = wrap_gutenberg_blocks(html)

    # Append FAQ schema as Custom HTML block
    if faq_schema:
        content += '\n\n' + faq_schema_block(faq_schema)

    return content

def get_or_create_category(name):
    """Get category ID by name, create if not exists."""
    r = requests.get(f"{WP_URL}/wp-json/wp/v2/categories?search={name}", headers=get_headers())
    cats = r.json()
    if cats:
        return cats[0]['id']
    r = requests.post(f"{WP_URL}/wp-json/wp/v2/categories",
                      headers=get_headers(), json={'name': name})
    return r.json().get('id')

def publish_draft(title, slug, meta_description, markdown_content, faq_schema, category=None):
    """Publish blog post as Draft to WordPress."""
    wp_content = markdown_to_wp_content(markdown_content, faq_schema)

    post_data = {
        'title': title,
        'slug': slug,
        'content': wp_content,
        'status': 'draft',
        'meta': {
            '_yoast_wpseo_metadesc': meta_description
        }
    }

    if category:
        cat_id = get_or_create_category(category)
        if cat_id:
            post_data['categories'] = [cat_id]

    r = requests.post(
        f"{WP_URL}/wp-json/wp/v2/posts",
        headers=get_headers(),
        json=post_data
    )

    if r.status_code in (200, 201):
        post = r.json()
        return post.get('id'), post.get('link'), f"{WP_URL}/wp-admin/post.php?post={post.get('id')}&action=edit"
    else:
        raise Exception(f"WordPress publish failed: {r.status_code} — {r.text[:300]}")
