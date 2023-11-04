def main():
    # coke price
    coke_price = 50
    print(f'Amount due: {coke_price}')
    coke = 50
    #insert coins into machine
    while True:
        # coin denominations
        coin = int(input('Insert Coins (5, 10, 25): '))

        if coin in (5,10, 25):
            coke -= coin
            if coke > 0:
                print(f'Amount Due: {coke}')
        else:
            continue
        # check to see if amount has reached 50
        if coke <= 0:
            break

    # give back change if needed

    if coke < 0:
        change = abs(coke)
        print(f'Change Owed: {change}')



main()


