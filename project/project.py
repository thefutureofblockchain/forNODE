import curses

def main(stdscr):
    # Clear screen
    stdscr.clear()

    stdscr.addstr("Pretty text", curses.color_pair(1))
    stdscr.refresh()
    stdscr.getkey()

curses.wrapper(main)