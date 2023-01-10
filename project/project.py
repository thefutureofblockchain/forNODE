import curses
from rich import print as rprint
def main(stdscr):
    # Clear screen
    stdscr.clear()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    stdscr.addstr("Pretty text", curses.color_pair(1))
    while True:
        c = stdscr.getkey()
        if c == "k":
            q = str(c)
            break
    stdscr.addstr(q)
    stdscr.refresh()
    stdscr.addstr(c)
    curses.echo()
    curses.flash()
    curses.echo()
    stdscr.refresh()

curses.wrapper(main)