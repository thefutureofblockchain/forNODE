from PIL import Image, ImageOps
import sys
import os

def main():
        #try:
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

            updatedb4 = ImageOps.fit(inp1 ,size, method=Image.Resampling.BICUBIC, bleed=0.0, centering=(0.5, 0.5))
            shirt.paste(updatedb4, mask = updatedb4)
            shirt.save(outp)
            inp1.close()
            shirt.close()
            '''except(FileNotFoundError,IndexError,ValueError):
            sys.exit("uh")'''
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





