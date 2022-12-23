def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if is_let(s) == True and is_6(s) == True and is_num(s) == True and is_period(s) == True:
        return True
    else:
        return False

def is_let(a):

def is_6(b):

def is_num(C):
def is_period(d):

main()