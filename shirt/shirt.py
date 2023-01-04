from PIL import Image, ImageOps
import sys
try:
        sys.argv[1] = sys.argv[1].lower()
        sys.argv[2] = sys.argv[2].lower()
        if len(sys.argv) != 3 or sys.argv[1].endswith("png") == False or sys.argv[1].endwith("jpeg") == False or sys.argv[1].endswith("jpg") == False or sys.argv[2].endswith("png") == False or sys.argv[2].endwith("jpeg") == False or sys.argv[2].endswith("jpg") == False or os.path.splitext:
            raise ValueError
        else:
            pass

except(FileNotFoundError,IndexError,ValueError):
    sys.exit("uh")

