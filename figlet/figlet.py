from pyfiglet import Figlet
import sys
#use sys.argv btwwww
figlet = Figlet()
#a  = figlet.getFonts()
s = input("Enter: ")\
a = figlet.getFonts(sys.argv[2])
print(a)
if len(sys.argv) == 2:
        #if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        s = input("Enter: ")
        a = figlet.getFonts(sys.argv[2])
        print(a)
        #s = figlet.setFont(font=sys.argv[2])
        print(s)
        #print(figlet.renderText(s))


