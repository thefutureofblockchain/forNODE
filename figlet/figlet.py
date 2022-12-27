from pyfiglet import Figlet
import sys
figlet = Figlet()
s = input("Enter: ")
if len(sys.argv) == 2 and sys.argv[1] == "-f" or sys.argv[1] == "--font":

        figlet.setFont(font = sys.argv[2])
        print(figlet.renderText(s))


