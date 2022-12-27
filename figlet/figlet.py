from pyfiglet import Figlet
import sys
figlet = Figlet()
print(len(sys.argv))
if len(sys.argv) == 3:
        print("truee")
        if sys.argv[2] == "-f" or sys.argv[2] == "--font":
                s = input("Enter: ")
                figlet.setFont(font = sys.argv[1])
                print(figlet.renderText(s))


