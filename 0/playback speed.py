#implement a program in Python that prompts the user for input and then outputs that same input,
# replacing each space with ... (i.e., three periods).

def main():
    user_input = input("Please enter your text:")
    modified_input = user_input.replace(' ', '...')
    print(modified_input)


main()

