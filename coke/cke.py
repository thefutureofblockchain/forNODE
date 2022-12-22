while True:
    n = int(input("Insert Coin: "))
    if n > 50:
        break
    elif n == 25 or n == 10 or n == 5:
        amtdue = 50 - n
        print("Amount due:" , amtdue)
        
sum = n-50
print("Change = ", sum)

