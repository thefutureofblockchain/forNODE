import curses
from rich import print as rprint
def main(stdscr):
    # Clear screen
    stdscr.clear()
    d = 0
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    stdscr.addstr("Pretty text", curses.color_pair(1))
    c = stdscr.getkey()
    if c == "k":
            q = str(c)
    stdscr.addstr(q)
    stdscr.refresh()
    stdscr.addstr(c)
    curses.echo()
    curses.flash()
    curses.echo()
    stdscr.refresh()

curses.wrapper(main)