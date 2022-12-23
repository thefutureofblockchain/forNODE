def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if is_num(s) == True:
        return True
    else:
        return False
def is_let(a):
    ba = a[0:2]
    if ba.isalpha() == True:
        return True
    else:
        return False
def is_6(b):
    if len(b) <= 6:
        return False
    else:
        return True

def is_period(d):
        if d.isalnum() == True:
            return True
        else:
            return False
def is_num(c):
    for letter in c:
        if letter.isdigit() == True:
            qa, b, d = c.partition(letter)
            if d.isdigit() == True or len(d)== 0:
                return True
            else:
                return False
main()