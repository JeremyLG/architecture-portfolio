import pynecone as pc

from .. import constants, styles

difficulty_colors = {"Beginner": "green", "Intermediate": "orange", "Advanced": "red"}


def gallery_card(gif, link, website):
    return pc.link(
        pc.text(
            website,
            font_family="Silkscreen",
        ),
        pc.box(
            pc.image(
                src=gif,
                height="18em",
            ),
            border_radius="1em",
            box_shadow=styles.DOC_SHADOW_DARK,
            overflow="hidden",
            _hover={
                "box_shadow": "0 0 .25em .11em #756AEE",
            },
        ),
        href=link,
    )


def index_gallery():
    return pc.box(
        pc.vstack(
            pc.text(
                "Gallery", font_size=styles.H2_FONT_SIZE, font_weight=styles.BOLD_WEIGHT
            ),
            pc.text(
                "See some projects I've already worked on. ",
                pc.link(
                    "View all projects portfolio →",
                    href=constants.PROJECTS_URL,
                    style=styles.LINK_STYLE,
                ),
                color="#676767",
            ),
            pc.center(
                pc.hstack(
                    *[
                        gallery_card(card["img"], card["id"], card["name"])
                        for card in constants.PROJECTS[:3]
                    ],
                    spacing="1em",
                    margin_top="1em",
                ),
                width="100%",
            ),
            align_items="left",
            border="1px solid #E3E3E3",
            box_shadow=styles.DOC_SHADOW_LIGHT,
            border_radius="12px",
            width="100%",
            padding=["1em", "2em"],
        ),
        width="100%",
        padding="1em",
    )


def component_grid():
    sidebar = []
    for project in constants.PROJECTS:
        sidebar.append(
            pc.link(
                pc.vstack(
                    pc.box(
                        height="20em",
                        width="20em",
                        background_image=project["img"],
                        background_size="cover",
                        background_repeat="no-repeat",
                        rounded="lg",
                    ),
                    pc.hstack(
                        pc.spacer(),
                        pc.badge(
                            project["difficulty"],
                            color_scheme=difficulty_colors[project["difficulty"]],
                        ),
                    ),
                    pc.heading(project["name"], style={"fontSize": "1.5em"}),
                    pc.box(
                        project["description"],
                        height="3em",
                        background="linear-gradient(transparent .5em, white)",
                    ),
                    pc.divider(),
                    pc.hstack(
                        *[
                            pc.badge(tag, border_radius="15px", padding_x=".5em")
                            for tag in project["tags"]
                        ],
                        padding_bottom=".5em",
                    ),
                    align_items="left",
                    row_span=3,
                    col_span=1,
                    box_shadow="lg",
                    border_radius="1em",
                    bg_color="white",
                    padding="1em",
                    _hover={
                        "box_shadow": "rgba(38, 57, 77, .3) 0px 20px 30px -10px",
                    },
                ),
                href=project.get("id"),
            )
        )
    return pc.box(
        pc.responsive_grid(*sidebar, columns=[1, 2, 2, 2, 3], gap=4),
    )


def gallery():
    return pc.flex(
        pc.hstack(
            pc.box(
                pc.heading("Gallery", first=True),
                pc.text("Here are some examples of what you can make with Pynecone. "),
                pc.divider(),
                component_grid(),
                text_align="left",
            ),
            align_items="start",
        ),
        flex_direction="column",
        height="100%",
        margin_bottom="4em",
    )
