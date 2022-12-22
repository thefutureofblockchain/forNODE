amtdue = 50
print("Amount Due:" , amtdue  )
coins = int(input("Insert Coin : "))
if coins == 25 or coins == 10 or coins == 5:
    while coins <= amtdue:
        amtdue = 50 - coins
        print("Amount due:" , amtdue)
        coins = int(input("Insert Coin : "))