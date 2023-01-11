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
    ques1():
    ques2():
    ques3():
    ques4():
    ques5():
    ques6():
    ques7():
    ques8():
    ques9():
    ques10():
def ques1():
    rich.print("Are you the kind of person who likes to be anxious?")
    while True:
        Ques1 = input(": ")
        a = Ques1.lower()
        if a != "y" and a != "n":
            rich.print("You did not enter a character that was y or n")
        else:
            break

if __name__ == "__main__":
    main()

