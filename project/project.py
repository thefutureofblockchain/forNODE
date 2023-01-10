import curses
from rich import print as rprint
def main(stdscr):
    # Clear screen
    stdscr.clear()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    stdscr.addstr("Pretty text", curses.color_pair(1))
    a = stdscr.getkey()
    stdscr.addstr(a)
    curses.echo()
    curses.flash()
    curses.echo()
    stdscr.refresh()
    stdscr.getkey()

curses.wrapper(main)