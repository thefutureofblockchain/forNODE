given = 0
to_get = 0
amtdue = 50
while True:
    coins = int(input("Insert Coin"))
    if coins == 25 or coins == 10 or coins == 5:
        given = to_get + coins
        amtdue = amtdue - given
    if amtdue > 0:
        print("amount due is ", amtdue)
    elif amtdue <= 0:
        change = amtdue*-1
        print("channge is", change)


