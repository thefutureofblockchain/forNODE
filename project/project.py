import curses
from rich import print as rprint
def main(stdscr):
    # Clear screen
    stdscr.clear()
    rprint("hello")
curses.wrapper(main)
