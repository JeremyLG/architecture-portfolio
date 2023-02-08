import pynecone as pc

from ..helpers import get_images


def project(path):
    return pc.vstack(
        pc.desktop_only(wrap_images(path)),
        pc.tablet_only(wrap_images(path), 3),
        pc.mobile_only(wrap_images(path, 2)),
    )


def wrap_images(path, columns=4):
    return pc.wrap(
        *[
            pc.wrap_item(pc.link(pc.image(src=image), href=image))
            for image in get_images(path)
        ],
        columns=[columns],
        align="center",
        spacing="2",
        padding="2em",
        width="100%",
    )
