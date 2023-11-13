def main():
    #        empty list to add items
    list = []

    while True:
        try:
             # ask for input and capitalize it
            items = input('').capitalize()


    #         add items to list
            list.append(items)
        except EOFError:
            break

            # Calculate and print the count for each item
    item_counts = {}
    for item in list:
        item_counts[item] = item_counts.get(item, 0) + 1

    # print out list
    for item, count in item_counts.items():
        print(f"{count} {item}")
main()
