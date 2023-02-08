"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
import pynecone as pc

from . import constants
from .navbar import navbar
from .pages import footer, gallery, index, project
from .state import State


def render_page(page):
    return pc.flex(
        navbar(),
        pc.box(
            page,
            footer(),
            max_width="80em",
            margin_x="2em",
            margin_top="5em",
        ),
    )


# Add state and page to the app.
app = pc.App(
    state=State,
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Silkscreen&display=swap",
    ],
)
app.add_page(render_page(index()), route="/")
app.add_page(render_page(gallery()), route=constants.PROJECTS_URL)

for project_dict in constants.PROJECTS:
    app.add_page(
        render_page(project(project_dict.get("path"))),
        route=f"""/{project_dict.get("id", "ta")}""",
    )
app.compile()
