from fasthtml.common import *
import os 
from utils import get_all_blogs 
from typing import Dict 
from models import BlogPost 
from utils import render_blog_post

blog_posts : Dict[str, BlogPost] = get_all_blogs()


app, rt = fast_app(hdrs=(
    Link(rel='stylesheet', href='https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&family=Playfair+Display:wght@400;700&display=swap'),
    Style("""
       
        .main-content {
            font-family: 'Outfit', sans-serif;
        }
    """)
))


# Helper function to create the menu
def create_menu():
    return Nav(
        Ul(
            Li(A("Home", href="/")),
            Li(A("Blog", href="/blog"))
        ),
        style="background-color: #f8f9fa; padding: 10px;",
        cls = "menu-nav"
    )

# Helper function to create the page layout
def page_layout(title, content):
    return Titled(
        title,
        create_menu(),
        Main(
            Container(content),
            style="margin-top: 20px;",
            cls = "main-content"
        )
    )

@rt("/")
def home():
    return page_layout(
        "",
        Div(
            Div(
                Div(
                Img(src="assets/Display_Picture.jpg",
                    alt="Me in Vienna",
                    style="width: 300px; height: 300px; object-fit: cover; border-radius: 50%;"),
                    style="float: right; margin-left: 20px; margin-bottom: 20px; width: 300px;"
                ),
                P("Hi I'm Sudarshan and this is my personal website!"),
                P(
                    "I write software for a living and currently work at ",
                    A("Clearfeed",href="https://clearfeed.ai"),
                    " as an AI/ML Engineer. I joined Clearfeed as an intern in my eighth semester of undergrad and have since been building the NLP pipeline that drives our product!",
                    "."
                ),
                P(
                    "Anyway, this website won't be too much about my work.",
                    Br(),
                    "A long list of (inexhaustive) things that I am interested in and hope to write about here  : ",
                    Ul(
                        Li(Em("Tennis"), " — I started playing tennis when I was six and continue to actively play the sport. I also (obsessively) follow the sport, and spend more time thinking about it than I'd like to admit"),

                        style="margin-top: 10px; margin-bottom: 10px;"
                    ),
                    Ul( 
                        Li(Em("Technology/Software")," — I am pretty early in my career as a software developer and intend to write about things that I learn along the way. It's also a particularly interesting time to be working in AI (more than half the code for this site was written by an LLM)"),
                        style="margin-top: 10px; margin-bottom: 10px;"
                    ), 
                    Ul(
                        Li(Em("Society/Politics/Culture"),"— I have several (possibly incorrect) opinions about the times we live in. While I am not brave enough to broadcast some of them publicly, I will attempt to put out what I can")
                    ),
                    Ul( 
                        Li(Em("Media/Literature"), "—  I like reading and watching movies/TV Shows (my Instagram screen time might suggest otherwise). ")
                    )
                ),
                P(
                    "Whether I will actually write at all about any of these things, I do not know.  But this is an honest attempt at becoming a better writer, and being actively engaged in the process of learning/thinking about new things. "
                ),
                Blockquote(
                    "''I am large. I contain multitudes.'",
                    Br(),
                    "    — Walt Whitman, Song of Myself ",
                    style="font-style: italic; margin: 20px 0; padding: 20px; border-left: 4px solid #ccc; background-color: #f9f9f9;"
                ),
                style="max-width: 800px; margin: 0 auto; padding: 20px; overflow: hidden;"
            ),
            
            style="display: flex; justify-content: center; align-items: flex-start;"
        )
    )

@rt("/blog")
def get():
    
    blog_list = Ul(
        *[Li(
            Article(
                H3(A(post.title, href=f"/blog/{slug}")),
                P(post.date.strftime('%B %d, %Y')),
                P(post.description, style="color: #666;"),
                Div(
                    *[Span(tag, style="background: #eee; padding: 2px 8px; border-radius: 12px; margin-right: 8px;")
                      for tag in post.tags],
                    style="margin-top: 8px;"
                ),
                style="margin-bottom: 2em;"
            )
        ) for slug, post in blog_posts.items()],
        style="list-style: none; padding: 0;"
    )
    
    return page_layout(
        "",
        Div(
            P("Welcome to my blog. This will be a collection of my various ramblings",
              style="font-size: 1.1rem; margin-bottom: 0.5rem;"),  # Increased font size
            Div(
                H3("Posts"),
                blog_list,
                style="max-width: 800px; margin: 0; padding: 20px;"  # Removed 'margin: 0 auto' to left-align
            )
        )
        
    )


@rt("/blog/{slug}")
def get(slug: str):
    try:
        post = blog_posts[slug]
        html_content = render_blog_post(post)
        return page_layout( 
            f"",
            NotStr(html_content)
        )
    except FileNotFoundError:
        return page_layout(
            "404 Not Found",
            P("Sorry, this blog post doesn't exist.")
        )
    
serve()