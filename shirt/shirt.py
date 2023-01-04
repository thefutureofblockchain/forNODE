from PIL import Image, ImageOps
import sys
try:
    def main():
        if is_valid(sys.argv) == False:
            raise ValueError
        else:
            pass
        
    def is_valid(n):
        n[1] = n[1].lower()
        n[2] = n[2].lower()
        if len(n) != 3 or n[1].endswith("png") == False or n[1].endwith("jpeg") == False or n[1].endswith("jpg")or n[2].endswith("png") == False or n[2].endwith("jpeg") == False or n[2].endswith("jpg") == False:
            return False
        else:
            return True
except(FileNotFoundError,IndexError,ValueError):
    sys.exit("uh")
