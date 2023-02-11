import pynecone as pc

from .state import State


def navbar_item(icon, title, href):
    return pc.link(
        pc.cond(
            State.sidebar_open,
            pc.hstack(
                pc.icon(tag=icon),
                pc.text(title, font_family="Silkscreen", size="sm"),
            ),
            pc.icon(tag=icon),
        ),
        href=f"/{href}",
        color="rgb(107,99,246)",
        button=True,
    )


def navbar():
    return pc.box(
        pc.vstack(
            pc.mobile_and_tablet(
                pc.icon(
                    tag="HamburgerIcon",
                    on_click=State.toggle_sidebar,
                    width="1.5em",
                    height="1.5em",
                    _hover={
                        "cursor": "pointer",
                    },
                ),
            ),
            pc.tablet_and_desktop(
                pc.vstack(
                    pc.heading("Ariane", font_family="Quicksand", size="lg"),
                    pc.heading("Michon", font_family="Quicksand", size="lg"),
                    align_items="stretch",
                ),
                pc.vstack(
                    navbar_item("StarIcon", "Home", ""),
                    navbar_item("CalendarIcon", "Projects", "projects"),
                    navbar_item("InfoIcon", "Info", "info"),
                    navbar_item("EmailIcon", "Contact", "contact"),
                    spacing="4",
                    align_items="stretch",
                ),
                pc.button(
                    pc.icon(tag="MoonIcon"),
                    on_click=pc.toggle_color_mode,
                ),
                spacing="10",
            ),
        ),
        backdrop_filter="blur(6px)",
        position="sticky",
        width="15%",
        padding_y="2em",
    )
