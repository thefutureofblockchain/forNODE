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

rich.print("[red]Hello!")
rich.print("[green]Are you ready?")
print("Y/N answers only!")
os.system('clear')
