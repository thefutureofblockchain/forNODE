from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Welcome, Static, Button
import random
import time


class EscapeRoomApp(App):
    """A Textual for a terminal based game."""
    def compose(self) -> ComposeResult:
        yield Welcome()
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

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()
        yield Static("Welcome.")
        yield Button("Yes", id="yes", variant="primary")
        yield Button("No", id="no", variant="error")
    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.exit(event.button.id)

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark
def main():
    EscapeRoomApp.on_mount()
    print("hello")
    EscapeRoomApp.on_mount()


if __name__ == "__main__":
    app = EscapeRoomApp()
    app.run()