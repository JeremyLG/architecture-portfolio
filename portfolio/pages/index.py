import pynecone as pc

from pcconfig import config
from .projects import index_gallery

docs_url = "https://pynecone.io/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


def index():
    return pc.vstack(
        pc.heading(
            "Welcome to my portfolio WIP, I'm Ariane Michon, a freelance architect!",
            font_size="2em",
        ),
        index_gallery(),
    )
