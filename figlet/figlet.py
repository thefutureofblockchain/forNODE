from pyfiglet import Figlet
import sys
figlet = Figlet()
if len(sys.argv) == 3:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
                s = input("Enter: ")
                figlet.setFont(font = sys.argv[2])
                print(figlet.renderText(s))
        else:
                sys.exit("First arguement wasn't appropriate")
else:
        sys.exit("Too many or too few arguements")


