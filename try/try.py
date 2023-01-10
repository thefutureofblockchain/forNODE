from textual.app import App, ComposeResult
from textual.widgets import Header, Footer
import random
import time


class EscapeRoomApp(App):
    """A Textual for a terminal based game."""
    COLORS = [
        "white",
        "maroon",
        "red",
        "purple",
        "fuchsia",
        "olive",
        "yellow",
        "navy",
        "teal",
        "aqua",
    ]

    def on_mount(self) -> None:
        colors = self.COLORS
        self.screen.styles.background = random.choice(colors)
        t
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark


if __name__ == "__main__":
    app = EscapeRoomApp()
    app.run()