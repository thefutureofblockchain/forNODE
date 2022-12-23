def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if is_let(s) == True and is_6(s) == True and is_num(s) == True and is_period(s) == True :
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
        return True
    else:
        return False

def is_period(d):
        if d.isalnum() == True:
            return True
        else:
            return False
def is_num(c):
    if c.isalpha() == True:
        return True
    else:
        for letter in c:
            if letter.isnumeric() == True:
                qa, b, d = c.partition(letter)
                if d.isdigit() == True and b!="0" or len(d)== 0:
                    return True
                else:
                    return False




main()