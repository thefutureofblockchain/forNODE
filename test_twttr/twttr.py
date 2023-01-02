import inflect
p = inflect.engine()
def main():

    q = input("Enter: ")
    ab = shorten(q)
    '''for letter in ab:
        return f"letter, sep = "", end = """'''
    print(ab)

def shorten(word):
    a = []
    for letter in word:
        if letter =="a" or letter =="e" or letter == "i" or letter == "o" or letter == "u" or letter =="A"or letter =="E"or letter =="I"or letter =="O"or letter =="U" :
            continue
        a.append(letter)

    #return a
    #for letter in a:
        #return letter
    ab = "".join(a)
    return ab
    #a = p.join(a)
    #return a
if __name__ == "__main__":
    main()