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
        href=href,
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
                    navbar_item("StarIcon", "Home", "/"),
                    navbar_item("CalendarIcon", "Projects", "/projects"),
                    navbar_item("InfoIcon", "Info", "/info"),
                    navbar_item("EmailIcon", "Contact", "/contact"),
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


def navbarb():
    return pc.box(
        pc.drawer(
            pc.drawer_content(sidebar_content()),
            auto_focus=False,
            is_open=True,
            placement="left",
            return_focus_on_close=False,
        ),
        width="15%",
        backdrop_filter="blur(6px)",
        position="sticky",
    )


def sidebar_content():
    return pc.box(
        pc.link(
            pc.flex(
                pc.icon(tag="StarIcon", mr="4", font_size="16"),
                pc.text("Home", font_family="Silkscreen", size="sm"),
                align="center",
                p="4",
                mx="4",
                border_radius="lg",
                role="group",
                cursor="pointer",
                _hover={
                    "bg": "cyan.400",
                    "color": "white",
                },
            )
        ),
        pc.link(
            pc.flex(
                pc.icon(tag="CalendarIcon", mr="4", font_size="16"),
                pc.text("Home", font_family="Silkscreen", size="sm"),
                align="center",
                p="4",
                mx="4",
                border_radius="lg",
                role="group",
                cursor="pointer",
                _hover={
                    "bg": "cyan.400",
                    "color": "white",
                },
            )
        ),
    )
