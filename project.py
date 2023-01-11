import rich
import os
import time
import sys
bp = 0
pf = 0
mun = 0
wsd = 0
def main():
    os.system("ls")
    os.system('clear')
    rich.print("[red]Hello!")
    rich.print("[green]Are you ready?")
    a = input("Y/N: ")
    if a != "y" and a.lower() != "n":
        sys.exit("Input was incorrect")
    os.system('clear')
    ques1()
    os.system('clear')
    ques2()
    os.system('clear')
    ques3()
    os.system('clear')
    ques4()
    os.system('clear')
    ques5()
    os.system('clear')
    ques6()
    os.system('clear')
    ques7()
    os.system('clear')
    ques8()
    os.system('clear')
    ques9()
    os.system('clear')
    ques10()
    os.system('clear')
    rich.print(" bp is",  bp ,", pf is",pf,"wsd is",wsd ," and lastly, mun is" ,mun)
def ques1():
    global bp
    global pf
    global mun
    global wsd
    rich.print("[green]Are you the kind of person who likes to be anxious?")
    while True:
        Ques1 = input(": ")
        a = Ques1.lower()
        if a != "y" and a != "n":
            rich.print("You did not enter a character that was y or n")
        else:
            break
    if a == "y":
        bp+=1
    else:
        pf+=1
        mun+=1
        wsd+=1
def ques2():
    global bp
    global pf
    global mun
    global wsd
    rich.print("Do you like to lie?")
    while True:
        Ques2 = input(": ")
        a = Ques2.lower()
        if a != "y" and a != "n":
            rich.print("You did not enter a character that was y or n")
        else:
            break
    if a == "y":
        bp+=1
        wsd+=1
        mun+=1
    else:
        pf+=1
def ques3():
    global bp
    global pf
    global mun
    global wsd
    rich.print("Facts(y) or logic(n)?")
    while True:
        Ques1 = input(": ")
        a = Ques1.lower()
        if a != "y" and a != "n":
            rich.print("You did not enter a character that was y or n")
        else:
            break
    if a == "y":
        pf+=1
        mun+=1
    else:
        bp+=1
        wsd+=1


def ques4():
    global bp
    global pf
    global mun
    global wsd
    rich.print("Do you have weird, what some might even call oddly specific knowledge?")
    while True:
        Ques1 = input(": ")
        a = Ques1.lower()
        if a != "y" and a != "n":
            rich.print("You did not enter a character that was y or n")
        else:
            break
    if a == "y":
        pf+=1
        mun+=1
    else:
        bp+=1
        wsd+=1
def ques5():
    global bp
    global pf
    global mun
    global wsd
    rich.print("Do you think the speed and quality of the speaker can make or break a debate?")
    while True:
        Ques1 = input(": ")
        a = Ques1.lower()
        if a != "y" and a != "n":
            rich.print("You did not enter a character that was y or n")
        else:
            break
    if a == "y":
        pf+=1
    else:
        bp+=1
        wsd+=1
        mun+=1
def ques6():
    global bp
    global pf
    global mun
    global wsd
    rich.print("Do you think the best things in life are short?")
    while True:
        Ques1 = input(": ")
        a = Ques1.lower()
        if a != "y" and a != "n":
            rich.print("You did not enter a character that was y or n")
        else:
            break
    if a == "y":
        pf+=1
        mun+=1
    else:
        bp+=1
        wsd+=1
def ques7():
    global bp
    global pf
    global mun
    global wsd
    rich.print("As a child, did you engage in pretend play much?")
    while True:
        Ques1 = input(": ")
        a = Ques1.lower()
        if a != "y" and a != "n":
            rich.print("You did not enter a character that was y or n")
        else:
            break
    if a == "y":
        mun+=1
    else:
        bp+=1
        wsd+=1
        pf+=1
def ques8():
    global bp
    global pf
    global mun
    global wsd
    rich.print("Are you okay with being left out?")
    while True:
        Ques1 = input(": ")
        a = Ques1.lower()
        if a != "y" and a != "n":
            rich.print("You did not enter a character that was y or n")
        else:
            break
    if a == "y":
        wsd+=1
    else:
        bp+=1
        mun+=1
        pf+=1
def ques9():
    global bp
    global pf
    global mun
    global wsd
    rich.print("Truthfully, do you think you are the best in your friend group?")
    while True:
        Ques1 = input(": ")
        a = Ques1.lower()
        if a != "y" and a != "n":
            rich.print("You did not enter a character that was y or n")
        else:
            break
    if a == "y":
        bp+=1
    else:
        pf+=1
        mun+=1
        wsd+=1
def ques10():
    global bp
    global pf
    global mun
    global wsd
    rich.print("Do you like to go into a situation fully prepared?")
    while True:
        Ques1 = input(": ")
        a = Ques1.lower()
        if a != "y" and a != "n":
            rich.print("You did not enter a character that was y or n")
        else:
            break
    if a == "y":
        pf+=1
        mun+=1
    else:
        wsd+=1
        bp+=1

if __name__ == "__main__":
    main()

