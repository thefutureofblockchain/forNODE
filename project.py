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
if __name__ == "__main__":
    main()

