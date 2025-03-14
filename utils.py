from pathlib import Path 
import markdown 
from datetime import datetime  
import os 
import re 
import yaml 
from typing import List 
from models import BlogPost 

# Create a custom Markdown instance with extensions for tables and code highlighting
md = markdown.Markdown(extensions=['tables', 'fenced_code', 'codehilite'])

def create_slug(title, date=None):
    """Create a slug from a title, optionally prepending the date."""
    basic_slug = title.lower().replace(" ", "-")
    
    # Remove any special characters that aren't appropriate for URLs
    basic_slug = re.sub(r'[^\w\-]', '', basic_slug)
    
    # If a date is provided, prepend it to the slug
    if date:
        if isinstance(date, datetime):
            date_str = date.strftime("%Y-%m-%d")
        else:
            # Try to parse the date if it's a string
            try:
                date_obj = datetime.fromisoformat(str(date))
                date_str = date_obj.strftime("%Y-%m-%d")
            except (ValueError, TypeError):
                # If date parsing fails, return just the basic slug
                return basic_slug
        
        return f"{date_str}-{basic_slug}"
    
    return basic_slug

def get_date(date_str) -> datetime : 
    print(f"Date string is {date_str}, its type is {type(date_str)}")
    if type(date_str) == str : 
        try:
            return datetime.fromisoformat(date_str)
        except ValueError:
            print(f"Error parsing date from string: {date_str}")
            # Try to parse date from string in case of error
            return datetime.now()
    elif type(date_str) == datetime : 
        return date_str
    elif type(date_str).__name__ == 'date':  # Handle datetime.date objects
        return datetime.combine(date_str, datetime.min.time())
    else : 
        print(f"None of the types match")
        return datetime.now()

def extract_date_from_slug(slug: str) -> datetime:
    """Extract date from slug if it's in common date formats."""
    try:
        # Check if slug starts with a date pattern: yyyy-mm-dd-
        date_pattern = re.match(r'^(\d{4}-\d{2}-\d{2})-', slug)
        if date_pattern:
            date_str = date_pattern.group(1)
            return datetime.fromisoformat(date_str)
        
        # Also check for other common formats
        # Format: dd-mm-yyyy-
        alt_pattern1 = re.match(r'^(\d{2}-\d{2}-\d{4})-', slug)
        if alt_pattern1:
            date_parts = alt_pattern1.group(1).split('-')
            if len(date_parts) == 3:
                day, month, year = date_parts
                return datetime(int(year), int(month), int(day))
        
        # Format: yyyymmdd-
        alt_pattern2 = re.match(r'^(\d{8})-', slug)
        if alt_pattern2:
            date_str = alt_pattern2.group(1)
            year = int(date_str[:4])
            month = int(date_str[4:6])
            day = int(date_str[6:8])
            return datetime(year, month, day)
    except Exception:
        # In case of any parsing error, log it and return None
        print(f"Error parsing date from slug: {slug}")
        pass
    
    return None

def get_blog_metadata(md_file_path) -> BlogPost : 
    with open(md_file_path, 'r', encoding='utf-8') as file : 
        content = file.read()
    
    frontmatter_match = re.match(r'^---\n(.*?)\n---\n(.*)', content, re.DOTALL) 
    if not frontmatter_match :  
        return None 
    
    frontmatter = yaml.safe_load(frontmatter_match.group(1))
    content = frontmatter_match.group(2)
    
    # First, try to get the date from frontmatter
    date_value = frontmatter.get('date', datetime.now())
    print(f"Date value is {date_value}")
    date = get_date(date_value)
    
    # Get or create the slug
    if 'slug' not in frontmatter : 
        frontmatter['slug'] = create_slug(frontmatter.get('title', 'Untitled'), date_value)
    
    # Do NOT extract date from slug since we already have it from frontmatter
    # and we don't want to override it with a potentially incorrect extraction
    print(f"Getting blog metadata for {md_file_path}, its date is {date}")

    return BlogPost(
        title=frontmatter.get('title', 'Untitled'),
        date=date,
        description=frontmatter.get('description', ''),
        tags=frontmatter.get('tags', []),
        content=content, 
        slug=frontmatter['slug']
    )        

def get_all_blogs() -> List[BlogPost] : 
    blogs_dir = Path('blogs')
    blogs = {}
    for md_file in blogs_dir.glob('*.md') : 
        if md_file.stem == 'template' : 
            continue 
        blog_data = get_blog_metadata(md_file)
        blogs[blog_data.slug] = blog_data 

    return dict(sorted(blogs.items(), key=lambda x: x[1].date, reverse=True))


def render_blog_post(post : BlogPost) -> str :
    # Convert markdown to HTML
    content_html = md.convert(post.content)
    
    # Format the date
    formatted_date = post.date.strftime('%B %d, %Y')
    
    # Check if there's a subtitle/deck in frontmatter
    subtitle_html = ""
    if hasattr(post, 'subtitle') and post.subtitle:
        subtitle_html = f'<div class="post-subtitle">{post.subtitle}</div>'
    
    # Featured image if available
    featured_image_html = ""
    if hasattr(post, 'featured_image') and post.featured_image:
        caption = getattr(post, 'image_caption', '')
        caption_html = f'<figcaption>{caption}</figcaption>' if caption else ''
        featured_image_html = f'''
        <figure class="featured-image">
            <img src="{post.featured_image}" alt="{post.title}" />
            {caption_html}
        </figure>
        '''
    
    # Add author byline if available
    author_html = ""
    if hasattr(post, 'author') and post.author:
        author_html = f'<div class="post-author">By {post.author}</div>'

    # Add a minimalist HTML structure without reading time
    return f"""
    <article class="blog-post">
        <header class="post-header">
            <h1 class="post-title">{post.title}</h1>
            {subtitle_html}
            <div class="post-meta">
                <time datetime="{post.date.isoformat()}">{formatted_date}</time>
            </div>
        </header>
        {featured_image_html}
        <div class="post-content">
            {content_html}
        </div>
    </article>
    """
