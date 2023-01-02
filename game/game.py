import random
def main():
    while True:
        try:
            lvl = int(input("Level: "))
            
            if lvl < 0:
                raise ValueError
            else:
                break
        except ValueError:
            continue
main()