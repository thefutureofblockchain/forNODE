from pyfiglet import Figlet
import sys
import random
figlet = Figlet()
if len(sys.argv) == 3:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
                s = input("Enter: ")
                figlet.setFont(font = sys.argv[2])
                print(figlet.renderText(s))
        else:
                sys.exit("First arguement wasn't appropriate")
elif len(sys.argv) == 1:
        s = input("Enter: ")
        a = random.randint(0, len(figlet.getFonts()))
        figlet.setFont(font = figlet.getFonts(a))
        print(figlet.renderText(s))
else:
        sys.exit("Too many or too few arguements")


