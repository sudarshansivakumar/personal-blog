from fasthtml.common import *
import os 
from utils import get_all_blogs 
from typing import Dict 
from models import BlogPost 
from utils import render_blog_post

blog_posts : Dict[str, BlogPost] = get_all_blogs()

# Define styles separately
font_link = Link(rel='stylesheet', href='https://fonts.googleapis.com/css2?family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&family=Source+Sans+Pro:wght@300;400;600&display=swap')

css_style = Style("""
        :root {
            --text-color: #1a1a1a;
            --light-gray: #f8f8f8;
            --border-color: #e0e0e0;
            --accent-color: #4a6fa5;
            --font-serif: 'Libre Baskerville', Georgia, serif;
            --font-sans: 'Source Sans Pro', sans-serif;
            --muted-text: #5a5a5a;
            --background-color: #fff;
        }
        
        body {
            font-family: var(--font-serif);
            line-height: 1.65;
            color: var(--text-color);
            background-color: var(--background-color);
            margin: 0;
            padding: 0;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0;
            background-color: var(--background-color);
            box-shadow: none;
            border: none;
        }
        
        .main-content {
            font-family: var(--font-serif);
            padding: 0;
            background-color: var(--background-color);
        }
        
        /* Navigation */
        .menu-nav {
            border-bottom: 1px solid var(--border-color);
            padding: 1.2rem 0;
            margin-bottom: 2.5rem;
            background-color: var(--background-color);
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
            margin-right: 2.5rem;
        }
        
        .menu-nav a {
            text-decoration: none;
            color: var(--text-color);
            font-weight: 600;
            font-size: 1rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            transition: color 0.2s;
            font-family: var(--font-sans);
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
        
        /* Blog content integration */
        .blog-content {
            max-width: 900px;
            margin: 0 auto;
            padding: 0 1.5rem;
            position: relative;
            background-color: transparent;
            box-shadow: none;
            border: none;
        }
        
        .blog-content img {
            max-width: 100%;
            height: auto;
            display: block;
            margin: 2rem auto;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
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
            background-color: #f9f9f9;
            padding: 1.2rem;
            border-radius: 0;
            overflow-x: auto;
            font-size: 0.9rem;
            margin: 2rem 0;
            border-left: 3px solid var(--accent-color);
            box-shadow: 0 1px 3px rgba(0,0,0,0.08);
        }
        
        code {
            font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
            background-color: rgba(0,0,0,0.03);
            padding: 2px 4px;
            border-radius: 2px;
            font-size: 0.9em;
        }
        
        pre code {
            padding: 0;
            background-color: transparent;
            color: #333;
            line-height: 1.6;
        }
        
        /* Add code title if specified */
        pre[data-code-title]:before {
            content: attr(data-code-title);
            display: block;
            padding: 0.5rem 1.2rem;
            margin: -1.2rem -1.2rem 1rem -1.2rem;
            background-color: rgba(0,0,0,0.05);
            font-family: var(--font-sans);
            font-size: 0.85rem;
            font-weight: 600;
            color: var(--muted-text);
            border-bottom: 1px solid rgba(0,0,0,0.1);
        }

        /* Add a full-width container for seamless layouts */
        .full-width-container {
            width: 100%;
            max-width: 100%;
            padding: 0;
            margin: 0;
            background-color: var(--background-color);
        }

        /* Remove any potential background color changes */
        .main-content > div {
            background-color: var(--background-color);
        }

        .main-content > div > div {
            background-color: var(--background-color);
        }

        /* Blog post specific styles */
        .post-header {
            margin-top: 40px;
            margin-bottom: 2.5rem;
            padding-bottom: 1.2rem;
            text-align: center;
            position: relative;
            border-bottom: none;
        }

        .post-header h1, .post-title {
            font-size: 2.2rem;
            line-height: 1.2;
            margin-bottom: 1.2rem;
            letter-spacing: -0.01em;
            font-weight: 700;
        }

        /* Blog articles styling */
        .blog-articles {
            display: flex;
            flex-direction: column;
            gap: 0.5rem;
        }

        .blog-article {
            margin-bottom: 1.5rem;
        }

        .blog-article h3 {
            font-size: 1.5rem;
            margin-bottom: 0.5rem;
            font-weight: 600;
        }

        .blog-article .blog-desc {
            color: var(--text-color);
            margin-bottom: 0.75rem;
            line-height: 1.5;
        }

        .blog-article .article-meta {
            font-size: 0.9rem;
            color: var(--muted-text);
            display: flex;
            align-items: center;
        }

        .blog-article .tag {
            display: inline-block;
            padding: 2px 8px;
            background-color: var(--light-gray);
            border-radius: 4px;
            margin-right: 0.5rem;
            font-size: 0.7rem;
            color: var(--accent-color);
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

        /* Restored blockquote styling */
        blockquote {
            font-family: var(--font-serif);
            font-style: italic;
            margin: 2rem 0;
            padding: 1.5rem 2rem;
            border-left: none;
            background-color: transparent;
            font-size: 1.15rem;
            color: var(--muted-text);
            position: relative;
            text-align: center;
        }

        blockquote::before,
        blockquote::after {
            content: '"';
            font-size: 3rem;
            color: var(--muted-text);
            opacity: 0.2;
            position: absolute;
            line-height: 1;
        }

        blockquote::before {
            top: -1rem;
            left: 0;
        }

        blockquote::after {
            content: '"';
            bottom: -2.5rem;
            right: 0;
        }

        /* Restored blog post layout */
        .post-header {
            margin-top: 40px;
            margin-bottom: 2.5rem;
            padding-bottom: 1.2rem;
            text-align: center;
            position: relative;
            border-bottom: none;
        }

        .post-header h1, .post-title {
            font-size: 2.2rem;
            line-height: 1.2;
            margin-bottom: 1.2rem;
            letter-spacing: -0.01em;
            font-weight: 700;
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

        /* Blog post styling */
        .blog-post {
            border: none;
            background-color: transparent;
            box-shadow: none;
            padding: 0;
        }

        .post-content {
            font-size: 1.15rem;
            line-height: 1.7;
        }

        .post-content .first-paragraph {
            font-size: 1.3rem;
            line-height: 1.6;
            margin-bottom: 2rem;
        }

        .post-content .first-paragraph::first-letter {
            float: left;
            font-size: 3.5rem;
            line-height: 1;
            padding: 0.1em 0.1em 0 0;
            font-weight: 700;
            color: var(--accent-color);
        }

        .post-content p {
            margin-bottom: 1.5rem;
        }

        .post-content h2 {
            font-size: 1.8rem;
            margin-top: 2.5rem;
            margin-bottom: 1.5rem;
            border-bottom: none;
            padding-bottom: 0;
        }

        .post-content h3 {
            font-size: 1.5rem;
            margin-top: 2rem;
            margin-bottom: 1.2rem;
        }

        .post-divider {
            width: 50px;
            height: 2px;
            background-color: var(--accent-color);
            margin: 0 auto 2rem;
        }

        /* Featured image styling */
        .featured-image {
            margin: 0 -2rem 3rem;
            width: calc(100% + 4rem);
            max-width: none;
        }

        .featured-image img {
            width: 100%;
            height: auto;
            margin: 0;
        }

        .featured-image figcaption {
            font-family: var(--font-sans);
            font-size: 0.85rem;
            color: var(--muted-text);
            text-align: right;
            padding: 0.5rem 1rem;
            font-style: italic;
        }

        /* Subtitle/deck styling */
        .post-subtitle {
            font-size: 1.4rem;
            line-height: 1.4;
            color: var(--muted-text);
            max-width: 85%;
            margin: 0 auto 1.5rem;
            font-style: italic;
        }

        /* Author byline */
        .post-author {
            font-family: var(--font-sans);
            font-size: 1rem;
            margin-bottom: 1rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }

        /* Pull quotes */
        .pull-quote {
            float: right;
            width: 40%;
            margin: 0.5rem -5% 2rem 2rem;
            padding: 0;
            font-size: 1.5rem;
            line-height: 1.4;
            text-align: left;
            border-top: 3px solid var(--accent-color);
            border-bottom: 1px solid var(--border-color);
            background: transparent;
        }

        .pull-quote p {
            padding: 1.5rem 0;
        }

        .pull-quote::before,
        .pull-quote::after {
            content: none;
        }

        .post-tags {
            margin: 1rem 0;
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
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
            Div(
                Container(content),
                cls="blog-post-wrapper"
            ),
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
            "A collection of my thoughts and explorations.",
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