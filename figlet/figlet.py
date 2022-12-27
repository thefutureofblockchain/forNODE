from pyfiglet import Figlet
import sys
#use sys.argv btwwww
figlet = Figlet()
#a  = figlet.getFonts()
###s = input("Enter: ")

#req_font = figlet.getFonts()
#print(req_font)
#a = req_font.index(sys.argv[2])
#print(a)

#if len(sys.argv) == 2:
        #if sys.argv[1] == "-f" or sys.argv[1] == "--font":
s = input("Enter: ")
figlet.setFont(font = sys.argv[2])
print(figlet.renderText(s))


