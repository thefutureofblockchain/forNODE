import curses
from rich import print as rprint
def main(stdscr):
    # Clear screen
    stdscr.clear()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    stdscr.addstr("Pretty text", curses.color_pair(1))
    begin_x = 20; begin_y = 7
    height = 5; width = 40
    win = curses.newwin(height, width, begin_y, begin_x)
    stdscr.refresh()
    stdscr.getkey()

curses.wrapper(main)