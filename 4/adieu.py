import inflect

p = inflect.engine()

# empty list to add names to
names = []

# infinite loop to keep asking for names
while True:
    try:

        # input to get names from user
        user_name = input('Name: ')

        # add name to list
        names.append(user_name)

    except (EOFError, KeyboardInterrupt):
        break

output = p.join(names)
print(f'adieu, adieu, to {output}')


