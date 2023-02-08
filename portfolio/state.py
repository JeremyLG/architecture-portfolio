import pynecone as pc


class State(pc.State):
    """The app state."""

    sidebar_open: bool = True

    def toggle_sidebar(self):
        self.sidebar_open = not self.sidebar_open
