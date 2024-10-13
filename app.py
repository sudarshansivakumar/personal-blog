from fasthtml.common import *
from routes.blog import setup_blog_routes
import os 

app, rt = fast_app()

# Helper function to create the menu
def create_menu():
    return Nav(
        Ul(
            Li(A("Home", href="/")),
            Li(A("Blog", href="/blog"))
        ),
        style="background-color: #f8f9fa; padding: 10px;"
    )

# Helper function to create the page layout
def page_layout(title, content):
    return Titled(
        title,
        create_menu(),
        Main(
            Container(content),
            style="margin-top: 20px;"
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
                    alt="Me in Prague",
                    style="width: 300px; height: 300px; object-fit: cover; border-radius: 50%;"),
                Figcaption("A picture of me in Vienna during the Summer of 2022, arguably the best summer of my life",
                           style="text-align: center; font-size: 0.9em; margin-top: 10px;"),
                    style="float: right; margin-left: 20px; margin-bottom: 20px; width: 300px;"
                ),
                P("Hi I'm Sudarshan! I am a software engineer by occupation, and hope to use this page to write about things that I find interesting."),
                P(
                    "I am currently an AI/ML Engineer at  ",
                    A("Clearfeed",href="https://clearfeed.ai"),
                    ", where I am broadly working on using NLP technologies to improve the efficiency of support agents on conversational platforms like Slack — this involves using state of the art ML models to build text classification, question answering, and search systems at scale.",
                    NotStr("<br>"),
                    "Or in other words, I build OpenAI wrappers for a living"
                ),
                P(
                    "I graduated with a major in Computer Science and Minor in Computational Mathematics from ",
                    A("MIT Manipal",href="https://www.manipal.edu/mit.html"),
                    " in July 2023. I spent the summer after my third year as a research intern at the ",
                    A("TrustHLT Lab",href="https://www.trusthlt.org/"),
                    " in TU Darmstadt through the WISE Scholarship funded by ",
                    A("DAAD",href="https://www.daad.in/en/"),
                    "."
                ),
                style="max-width: 800px; margin: 0 auto; padding: 20px; overflow: hidden;"
            ),
            style="display: flex; justify-content: center; align-items: flex-start;"
        )
    )

@rt("/blog")
def get():
    return page_layout(
        "",
        Div(
            P("Welcome to my blog. This will be a collection of my various ramblings")
        )
    )

@rt("/blog/{post_id}")
def get(post_id: str):
    try:
        with open(f"blogs/{post_id}.html", "r") as file:
            content = file.read()
        return page_layout(
            f"Blog Post: {post_id}",
            NotStr(content)
        )
    except FileNotFoundError:
        return page_layout(
            "404 Not Found",
            P("Sorry, this blog post doesn't exist.")
        )
    
serve()