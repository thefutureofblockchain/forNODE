from PIL import Image, ImageOps
import sys
import os
#try:
def main():
        inp = sys.argv[1]
        outp = sys.argv[2]
        sys.argv[1] = sys.argv[1].lower()
        sys.argv[2] = sys.argv[2].lower()
        if len(sys.argv) != 3 or sys.argv[1].endswith("png","jpeg","jpg") == False or sys.argv[2].endswith("png","jpeg","Jpg") == False:
            raise ValueError
        else:
            pass
        shirt = Image.open("shirt.png")
        inp1 = Image.open(inp)
        size = shirt.size
        size2 = inp1.size

        updatedshirt = ImageOps.fit(shirt,size2, method=Image.Resampling.BICUBIC, bleed=0.0, centering=(0.5, 0.5))
        inp1.paste(updatedshirt, updatedshirt)
        inp1.save(outp)
def osthing(a,b):
    ab, ba = os.path.splitext(a)
    aba , baa = os.path.splitext(b)
    if ba != baa:
        return False
    else:
        return True
main()



#except(FileNotFoundError,IndexError,ValueError):
   # sys.exit("uh")

