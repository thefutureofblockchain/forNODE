from pyfiglet import Figlet
import sys
#use sys.argv btwwww
figlet = Figlet()
#a  = figlet.getFonts()
s = input("Enter: ")
sys.argv[2] = sys.argv[2]
req_font = figlet.getFonts()
print(req_font)
print(req_font[sys.argv[2]])
if len(sys.argv) == 2:
        #if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        s = input("Enter: ")
        a = figlet.getFonts(sys.argv[2])
        print(a)
        #s = figlet.setFont(font=sys.argv[2])
        print(s)
        #print(figlet.renderText(s))


