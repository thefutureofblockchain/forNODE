import curses
from rich import print as rprint
def main(stdscr):
    # Clear screen
    stdscr.clear()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    stdscr.addstr("Pretty text", curses.color_pair(1))
    curses.echo()
    while True:
        c = stdscr.getch()
        if c == "p":
            stdscr.addstr("hi")
            stdscr.refresh()
            stdscr.addstr("hi")
        else:
            break
    curses.echo()
    stdscr.refresh()
    stdscr.getkey()

curses.wrapper(main)