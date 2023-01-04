from PIL import Image, ImageOps
import sys
import os
#try:
def main():
        inp = sys.argv[1]
        outp = sys.argv[2]
        sys.argv[1] = sys.argv[1].lower()
        sys.argv[2] = sys.argv[2].lower()
        '''if len(sys.argv) != 3 or sys.argv[1].endswith("png") == False or sys.argv[1].endswith("jpeg") == False or sys.argv[1].endswith("jpg") == False or sys.argv[2].endswith("png") == False or sys.argv[2].endwith("jpeg") == False or sys.argv[2].endswith("jpg") == False or os.path.splitext(sys.argv[1]) != os.path.splitext(sys.argv[2]):
            raise ValueError
        else:
            pass'''
        shirt = Image.open("shirt.png")
        inp1 = Image.open(inp)
        size = shirt.size
        size2 = inp1.size

        inpp = ImageOps.fit(shirt,size2, method=Image.Resampling.BICUBIC, bleed=0.0, centering=(0.5, 0.5))
        inpp.paste(shirt, shirt)
        print(size2, size)
        inpp.save(outp)
main()



#except(FileNotFoundError,IndexError,ValueError):
   # sys.exit("uh")

