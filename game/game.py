import random
import sys
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
    r = random.randint(1, lvl)
    while True:
        try:
            g = int(input("Guess: "))
            if g == r:
                print("Just right!")
                sys.exit("")
            elif g > r:
                print("Too Large!")
            elif g < r:
                print("Too small!")
            else:
                raise ValueError
        except ValueError:
            continue

main()