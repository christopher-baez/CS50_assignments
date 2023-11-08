def main():
    # get user input
    vanity = input('Plate: ').upper()
    # check for number and alphabet only
    if not vanity.isalnum():
        print('Invalid')
        return False
    # starts with 2 letters
    if not vanity[:2].isalpha():
        print('Invalid')
        return False
    # checking len between 2 and 6
    if not 2 <= len(vanity) <= 6:
        print('Invalid')
        return False
    # first number can't be 0 and subsequent must be digits
    for i, char in enumerate(vanity):
        if char.isdigit():
            if i == 0 or (i == 2 and char == '0'):  # Check for first digit not being '0'
                print('Invalid')
                return False
            if not vanity[i:].isdigit():  # After first digit, all must be digits
                print('Invalid')
                return False
            break  # Exit loop after finding the first digit, since the rest is checked
    print('Valid')  # If all checks are passed
    return True

main()
