from PIL import Image, ImageOps
import sys
import os

def main():
        try:
            inp = sys.argv[1]
            outp = sys.argv[2]
            sys.argv[1] = sys.argv[1].lower()
            sys.argv[2] = sys.argv[2].lower()
            if len(sys.argv) != 3 or ex(sys.argv[1],sys.argv[2]) or osthing(inp,outp) == False:
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
            Image.close(inp1,shirt)
        except(FileNotFoundError,IndexError,ValueError):
            sys.exit("uh")
def osthing(a,b):
        ab, ba = os.path.splitext(a)
        aba , baa = os.path.splitext(b)
        if ba != baa:
            return False
        else:
            return True
def ex(a , b):
        a = os.path.splitext(a)
        b = os.path.splitext(b)
        ba = [".png",".jpg",".jpeg"]
        if not a in ba or not b in ba:
            return False
        else:
            return True

main()





