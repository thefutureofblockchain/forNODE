import rich
import os
import time
import curses
os.system("ls")
time.sleep(2)
os.system('clear')
def main(stdscr):
    # Clear screen
    stdscr.clear()

rich.print("[red]hello")
rich.print("welcome to the day that might be your very last")