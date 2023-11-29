def is_valid(s):
    # Check for number and alphabet only
    if not s.isalnum():
        return False
    # Starts with 2 letters
    if not s[:2].isalpha():
        return False
    # Checking length between 2 and 6
    if not 2 <= len(s) <= 6:
        return False
    # First number can't be 0 and subsequent must be digits
    for i, char in enumerate(s):
        if char.isdigit():
            if i == 0 or (i == 2 and char == '0'):  # Check for first digit not being '0'
                return False
            if not s[i:].isdigit():  # After first digit, all must be digits
                return False
            break  # Exit loop after finding the first digit
    return True

def main():
    # Get user input
    vanity = input('Plate: ').upper()
    # Validate the plate
    if is_valid(vanity):
        print('Valid')
    else:
        print('Invalid')

if __name__ == "__main__":
    main()
