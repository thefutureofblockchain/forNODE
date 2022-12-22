while True:
    n = int(input("Insert Coin: "))
    if n != 25 or n != 10 or n != 5:
        amtdue = 50 - n
        print("Amount due:" , amtdue)
        x = int(input("Insert Coin: "))
        amtdue = amtdue - n+x
        print("Amount due: ", amtdue)
        y = int(input("Insert Coin: "))
        amtdue = amtdue - amtdue+y
        print("Amount due: ", amtdue)
'''sum = n-50
print("Change = ", sum)
'''
