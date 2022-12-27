from pyfiglet import Figlet
import sys
import random
figlet = Figlet()

b = len(figlet.getFonts())
a = random.randint(0, b)
c = figlet.getFonts()
if len(sys.argv) == 3:
                if sys.argv[1] == "-f" or sys.argv[1] == "--font" and c.count(sys.argv[2]) != 0:
                        s = input("Enter: ")
                        figlet.setFont(font = sys.argv[2])
                        print(figlet.renderText(s))
                else:
                        sys.exit("First arguement wasn't appropriate")
elif len(sys.argv) == 1:
                s = input("Enter: ")
                d = c[a]
                figlet.setFont(font = d)
                print(figlet.renderText(s))
else:
                sys.exit("Too many or too few arguements")




