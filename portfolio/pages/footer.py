import pynecone as pc

from .. import styles

footer_item_style = {
    "font_family": "Inter",
    "font_weight": "500",
    "_hover": {"color": styles.ACCENT_COLOR},
}

footer_style = {
    "box_shadow": "medium-lg",
    "border_top": "0.2em solid #F0F0F0",
    "vertical_align": "bottom",
    "padding_top": "4em",
    "padding_bottom": "2em",
    "padding_x": styles.PADDING_X2,
    "bg": "white",
}


def footer(style=footer_style):
    return pc.box(
        pc.vstack(
            pc.hstack(
                pc.vstack(
                    pc.text("Site", color=styles.SUBHEADING_COLOR),
                    pc.link("Home", href="indexpath", style=footer_item_style),
                    pc.link("Gallery", href="gallery.path", style=footer_item_style),
                    pc.link("Hosting", href="deploy.path", style=footer_item_style),
                    align_items="start",
                ),
                pc.vstack(
                    pc.text("Documentation", color=styles.SUBHEADING_COLOR),
                    pc.link(
                        "Introduction",
                        href="introduction.path",
                        style=footer_item_style,
                    ),
                    pc.link(
                        "Installation",
                        href="installation.path",
                        style=footer_item_style,
                    ),
                    pc.link("Components", href="library.path", style=footer_item_style),
                    align_items="start",
                ),
                pc.vstack(
                    pc.text("Resources", color=styles.SUBHEADING_COLOR),
                    pc.link(
                        "Github",
                        href="constants.GITHUB_URL",
                        style=footer_item_style,
                    ),
                    pc.link(
                        "Discord",
                        href="constants.DISCORD_URL",
                        style=footer_item_style,
                    ),
                    pc.link(
                        "Twitter",
                        href="constants.TWITTER_URL",
                        style=footer_item_style,
                    ),
                    align_items="start",
                ),
                justify="space-between",
                color=styles.LIGHT_TEXT_COLOR,
                align_items="top",
                padding_bottom="3em",
                min_width="100%",
            ),
            pc.hstack(
                pc.text(
                    "Copyright © 2023 Pynecone",
                    font_weight="500",
                ),
                pc.link(
                    "Contact",
                    href="constants.CONTACT_URL",
                    font_weight="500",
                    style=footer_item_style,
                ),
                justify="space-between",
                color=styles.LIGHT_TEXT_COLOR,
                padding_bottom="2em",
                min_width="100%",
            ),
        ),
        **style,
    )
