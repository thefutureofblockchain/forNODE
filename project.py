import rich
import os
import time
import sys
def main():
    os.system("ls")
    time.sleep(2)
    os.system('clear')
    rich.print("[red]Hello!")
    rich.print("[green]Are you ready?")
    a = input("Y/N: ")
    if a != "y" and a.lower() != "n":
        sys.exit("Input was incorrect")
    os.system('clear')

