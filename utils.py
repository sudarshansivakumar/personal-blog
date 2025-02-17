from pathlib import Path 
import markdown 
from datetime import datetime  
import os 
import re 
import yaml 
from typing import List 
from models import BlogPost 

md = markdown.Markdown()

def create_slug(title) : 
    return title.lower().replace(" ", "-")

def get_date(date_str) -> datetime : 
    if type(date_str) == str : 
        return datetime.fromisoformat(date_str)
    elif type(date_str) == datetime : 
        return date_str
    else : 
        return datetime.now()

def get_blog_metadata(md_file_path) -> BlogPost : 
    with open(md_file_path, 'r', encoding='utf-8') as file : 
        content = file.read()
    
    frontmatter_match = re.match(r'^---\n(.*?)\n---\n(.*)', content, re.DOTALL) 
    if not frontmatter_match :  
        return None 
    
    frontmatter = yaml.safe_load(frontmatter_match.group(1))
    content = frontmatter_match.group(2)
    if 'slug' not in frontmatter : 
        frontmatter['slug'] = create_slug(frontmatter.get('title', 'Untitled'))
    
    return BlogPost(
        title=frontmatter.get('title', 'Untitled'),
        date=get_date(frontmatter.get('date', datetime.now())),
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
    
    content_html = md.convert(post.content)
    return f"""
    <h1>{post.title}</h1>
    <p>{post.date.strftime('%B %d, %Y')}</p>
    <div>{content_html}</div>
    """
