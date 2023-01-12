import sys

def status(percent):
    sys.stdout.write("%3d%%\r" % percent)
    sys.stdout.flush()
status(4)