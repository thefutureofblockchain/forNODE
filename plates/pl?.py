for letter in "NRVOUS":
        if letter.isdigit() == True:
            qa, ba, da = "NRVOUS".partition(letter)
            if ba == 0 or ba == "0":
                print("f")
                break
            if da.isdigit() == True or len(da)== 0:
                print("True")
            else:
                print("F")
        else:
            print("t")
