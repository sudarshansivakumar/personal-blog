from fasthtml.common import *
import os 
from utils import get_all_blogs 
from typing import Dict 
from models import BlogPost 
from utils import render_blog_post

blog_posts : Dict[str, BlogPost] = get_all_blogs()

# Define styles separately
font_link = Link(rel='stylesheet', href='https://fonts.googleapis.com/css2?family=Domine:wght@400;700&family=Source+Sans+Pro:wght@300;400;600&display=swap')

css_style = Style("""
        :root {
            --text-color: #333;
            --light-gray: #f5f5f5;
            --border-color: #eaeaea;
            --accent-color: #2d72d9;
            --font-serif: 'Domine', Georgia, serif;
            --font-sans: 'Source Sans Pro', sans-serif;
            --muted-text: #666;
        }
        
        body {
            font-family: var(--font-sans);
            line-height: 1.6;
            color: var(--text-color);
            background-color: #fff;
            margin: 0;
            padding: 0;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 1.5rem;
        }
        
        .main-content {
            font-family: var(--font-sans);
        }
        
        /* Navigation */
        .menu-nav {
            border-bottom: 1px solid var(--border-color);
            padding: 1rem 0;
            margin-bottom: 2rem;
            background-color: #fff;
        }
        
        .menu-nav ul {
            display: flex;
            list-style: none;
            margin: 0;
            padding: 0;
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 1.5rem;
        }
        
        .menu-nav li {
            margin-right: 2rem;
        }
        
        .menu-nav a {
            text-decoration: none;
            color: var(--text-color);
            font-weight: 600;
            font-size: 1.1rem;
            transition: color 0.2s;
        }
        
        .menu-nav a:hover {
            color: var(--accent-color);
        }
        
        /* Typography */
        h1, h2, h3, h4, h5, h6 {
            font-family: var(--font-serif);
            margin-top: 2rem;
            margin-bottom: 1rem;
            line-height: 1.3;
        }
        
        h1 {
            font-size: 2.5rem;
            margin-top: 0;
        }
        
        h2 {
            font-size: 2rem;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 0.5rem;
        }
        
        h3 {
            font-size: 1.5rem;
        }
        
        p {
            margin-bottom: 1.5rem;
            font-size: 1.1rem;
        }
        
        /* Blog list styling */
        .blog-list {
            list-style: none;
            padding: 0;
            margin-top: 2rem;
        }
        
        .blog-list li {
            transition: transform 0.2s ease;
        }
        
        .blog-list li:hover {
            transform: translateX(3px);
        }
        
        .blog-list article {
            margin-bottom: 1.25rem;
            padding-bottom: 1.25rem;
            border-bottom: 1px solid var(--border-color);
            display: flex;
            align-items: flex-start;
            gap: 1.5rem;
        }
        
        .blog-list .article-main {
            flex: 1;
        }
        
        .blog-list .article-meta {
            width: 130px;
            text-align: right;
            font-size: 0.85rem;
        }
        
        .blog-list h3 {
            margin-top: 0;
            margin-bottom: 0.3rem;
            font-size: 1.6rem;
            letter-spacing: -0.02em;
            line-height: 1.2;
        }
        
        .blog-list h3 a {
            text-decoration: none;
            color: var(--text-color);
            transition: color 0.2s;
            position: relative;
        }
        
        .blog-list h3 a:hover {
            color: var(--accent-color);
        }
        
        .blog-list h3 a::after {
            content: '';
            position: absolute;
            bottom: -2px;
            left: 0;
            width: 0;
            height: 1px;
            background-color: var(--accent-color);
            transition: width 0.3s ease;
        }
        
        .blog-list h3 a:hover::after {
            width: 100%;
        }
        
        .blog-meta {
            margin-bottom: 0.5rem;
            color: var(--muted-text);
        }
        
        .blog-date {
            font-size: 0.85rem;
            font-style: italic;
        }
        
        .reading-time {
            display: block;
            font-size: 0.8rem;
            color: var(--muted-text);
            margin-top: 0.25rem;
        }
        
        .blog-desc {
            font-size: 1rem;
            margin-bottom: 0.75rem;
            line-height: 1.4;
            color: #444;
        }
        
        .tag-container {
            display: flex;
            flex-wrap: wrap;
            gap: 0.35rem;
            margin-top: 0.75rem;
        }
        
        .tag {
            background: var(--light-gray);
            padding: 2px 6px;
            border-radius: 3px;
            font-size: 0.7rem;
            color: var(--muted-text);
            text-transform: uppercase;
            letter-spacing: 0.02em;
        }
        
        @media (max-width: 768px) {
            .blog-list article {
                flex-direction: column;
                gap: 0.5rem;
            }
            
            .blog-list .article-meta {
                width: 100%;
                text-align: left;
                order: -1;
            }
        }
        
        /* Home page */
        .profile-picture {
            float: right;
            margin-left: 2rem;
            margin-bottom: 1.5rem;
            width: 250px;
            height: 250px;
            object-fit: cover;
            border-radius: 50%;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            /* Add these properties to ensure a perfect circle */
            aspect-ratio: 1;
            overflow: hidden;
            display: block;
        }

        
        blockquote {
            font-family: var(--font-serif);
            font-style: italic;
            margin: 2rem 0;
            padding: 1.5rem;
            border-left: 4px solid var(--accent-color);
            background-color: var(--light-gray);
            font-size: 1.2rem;
            color: #444;
        }
        
        /* Tables (CSV) */
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 2rem 0;
            font-size: 0.95rem;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        }
        
        th {
            background-color: var(--light-gray);
            font-weight: 600;
            text-align: left;
            padding: 0.85rem 1rem;
            border-bottom: 2px solid var(--border-color);
            color: #333;
            font-family: var(--font-serif);
        }
        
        td {
            padding: 0.75rem 1rem;
            border-bottom: 1px solid var(--border-color);
            vertical-align: middle;
        }
        
        tr:nth-child(even) {
            background-color: var(--light-gray);
        }
        
        tr:hover {
            background-color: rgba(45, 114, 217, 0.05);
        }
        
        caption {
            font-style: italic;
            margin-bottom: 0.75rem;
            color: var(--muted-text);
            text-align: left;
            font-size: 0.9rem;
        }
        
        /* Blog post content */
        .blog-content {
            max-width: 800px;
            margin: 0 auto;
        }
        
        .blog-content img {
            max-width: 100%;
            height: auto;
            display: block;
            margin: 1.5rem auto;
        }
        
        .blog-content a {
            color: var(--accent-color);
            text-decoration: none;
            border-bottom: 1px solid transparent;
            transition: border-color 0.2s;
        }
        
        .blog-content a:hover {
            border-color: var(--accent-color);
        }
        
        /* Code blocks */
        pre {
            background-color: var(--light-gray);
            padding: 1rem;
            border-radius: 4px;
            overflow-x: auto;
            font-size: 0.9rem;
            margin: 1.5rem 0;
        }
        
        code {
            font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
            background-color: var(--light-gray);
            padding: 2px 4px;
            border-radius: 3px;
            font-size: 0.9em;
        }
        
        pre code {
            padding: 0;
            background-color: transparent;
        }
        
        /* Blog post specific styles */
        .post-header {
            margin-bottom: 2rem;
            padding-bottom: 0.5rem;
        }
        
        .post-meta {
            display: flex;
            align-items: center;
            color: var(--muted-text);
            font-size: 0.9rem;
            margin: 0.75rem 0 1rem;
        }
        
        .post-meta time {
            margin-right: 1.5rem;
            font-style: italic;
        }
        
        .reading-time {
            position: relative;
            padding-left: 1.5rem;
        }
        
        .reading-time::before {
            content: "";
            position: absolute;
            left: 0.5rem;
            top: 50%;
            transform: translateY(-50%);
            width: 3px;
            height: 3px;
            background-color: var(--muted-text);
            border-radius: 50%;
        }
        
        .post-tags {
            margin: 1rem 0;
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
        }
        
        .post-divider {
            width: 50px;
            height: 3px;
            background-color: var(--accent-color);
            margin: 1.5rem 0;
        }
        
        .post-content {
            font-size: 1.1rem;
            line-height: 1.7;
        }
        
        .post-content .first-paragraph {
            font-size: 1.25rem;
            line-height: 1.6;
            color: #444;
        }
        
        .post-content p {
            margin-bottom: 1.5rem;
        }
        
        .post-content blockquote {
            margin: 2rem 0;
            padding: 1.5rem 2rem;
            position: relative;
            font-size: 1.15rem;
        }
        
        .post-content blockquote::before {
            content: "";
            position: absolute;
            left: -10px;
            top: -10px;
            font-size: 3rem;
            color: var(--accent-color);
            opacity: 0.3;
            font-family: var(--font-serif);
        }
        
        .post-footer {
            margin-top: 3rem;
            padding-top: 1rem;
        }
        
        .post-signature {
            font-style: italic;
            color: var(--muted-text);
            text-align: right;
        }
""")

# Initialize the app with separate headers
app, rt = fast_app(hdrs=[font_link, css_style])

# Helper function to create the menu
def create_menu():
    return Nav(
        Ul(
            Li(A("Home", href="/")),
            Li(A("Blog", href="/blog"))
        ),
        cls="menu-nav"
    )

# Helper function to create the page layout
def page_layout(title, content):
    return Titled(
        title,
        create_menu(),
        Main(
            Container(content),
            cls="main-content"
        )
    )

@rt("/")
def home():
    content_div = Div(
        Img(
            src="assets/Display_Picture.jpg",
            alt="Me in Vienna",
            cls="profile-picture"
        ),
        H1("Hi, I'm Sudarshan", style="font-size: 2.0rem; margin-bottom: 1rem;"),
        P("Welcome to the repository of my intrusive thoughts"),
        P(
            "I write software for a living and currently work at ",
            A("Clearfeed", href="https://clearfeed.ai"),
            " as an AI/ML Engineer. I joined Clearfeed as an intern in my eighth semester of undergrad and have since been building the NLP pipeline that drives our product!"
        ),
        P(
            "Anyway, this website won't be too much about my work. ",
            "A long list of (inexhaustive) things that I am interested in and hope to write about here:"
        ),
        Ul(
            Li(
                Strong("Tennis"), 
                " — I started playing tennis when I was six and continue to actively play the sport. I also (obsessively) follow the sport, and spend more time thinking about it than I'd like to admit"
            ),
            Li(
                Strong("Technology/Software"), 
                " — I am pretty early in my career as a software developer and intend to write about things that I learn along the way. It's also a particularly interesting time to be working in AI (more than half the code for this site was written by an LLM)"
            ),
            Li(
                Strong("Society/Politics/Culture"), 
                "— I have several (possibly incorrect) opinions about the times we live in. While I am not brave enough to broadcast some of them publicly, I will attempt to put out what I can"
            ),
            Li(
                Strong("Media/Literature"), 
                "—  I like reading and watching movies/TV Shows (my Instagram screen time might suggest otherwise)."
            ),
            style="margin: 1.5rem 0; padding-left: 1.5rem;"
        ),
        P(
            "Whether I will actually write at all about any of these things, I do not know. But this is an honest attempt at becoming a better writer, and being actively engaged in the process of learning/thinking about new things."
        ),
        Blockquote(
            '"I am large. I contain multitudes."',
            Br(),
            "— Walt Whitman, Song of Myself"
        ),
        cls="blog-content"
    )
    
    return page_layout(
        "",
        content_div
    )

@rt("/blog")
def get():
    blog_items = []
    
    for slug, post in blog_posts.items():
        # Use a more accurate reading time calculation
        word_count = len(post.content.split())
        # Count code blocks and tables which take longer to read
        code_block_count = post.content.count("```")
        table_row_count = post.content.count("|")
        
        # Basic reading time based on words
        reading_time = max(1, round(word_count / 200))
        
        # Add additional time for code blocks and tables
        if code_block_count > 0:
            reading_time += 1
        if table_row_count > 10:
            reading_time += 1
        
        article = Article(
            Div(
                H3(A(post.title, href=f"/blog/{slug}")),
                P(post.description, cls="blog-desc"),
                Div(
                    *[Span(tag, cls="tag") for tag in post.tags],
                    cls="tag-container"
                ) if post.tags else "",
                cls="article-main"
            ),
            Div(
                P(post.date.strftime('%b %d, %Y'), cls="blog-date"),
                Span(f"{reading_time} min read", cls="reading-time"),
                cls="article-meta"
            )
        )
        blog_items.append(Li(article))
    
    blog_list = Ul(*blog_items, cls="blog-list")
    
    page_content = Div(
        P(
            "A collection of my various ramblings.",
            style="font-size: 1.2rem; margin-bottom: 1rem; font-style: italic; color: var(--muted-text);"
        ),
        Div(style="width: 50px; height: 3px; background-color: var(--accent-color); margin-bottom: 2rem;"),
        blog_list,
        cls="blog-content"
    )
    
    return page_layout(
        "",
        page_content
    )


@rt("/blog/{slug}")
def get(slug: str):
    try:
        post = blog_posts[slug]
        html_content = render_blog_post(post)
        blog_content = Div(
            NotStr(html_content),
            cls="blog-content"
        )
        
        return page_layout( 
            f"",
            blog_content
        )
    except FileNotFoundError:
        error_content = Div(
            H1("404: Post Not Found"),
            P("Sorry, this blog post doesn't exist."),
            cls="blog-content"
        )
        
        return page_layout(
            "404 Not Found",
            error_content
        )
    
serve()