import curses

def main(stdscr):
    # Clear screen
    stdscr.clear()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
    stdscr.addstr("Pretty text", curses.color_pair(1))
    stdscr.refresh()
    stdscr.getkey()

curses.wrapper(main)