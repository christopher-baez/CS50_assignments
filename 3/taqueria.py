def main():
    # taqueria menu
    menu_regular = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    # creating menu lower case
    menu = {x.lower(): y for x, y in menu_regular.items()}

    # empty variable to add total to
    total = 0.0

    while True:
        try:
            # getting input and turning it lowercase
            item = input('Item: ').lower()

            # loop to check items and print total
            if item in menu:
                total += menu[item]
                print(f'${round(total, 2)}')
        except EOFError:
            break
        except KeyError:
            pass


main()
