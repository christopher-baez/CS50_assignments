# get input name
def main():
    names = input("camelCase: ")

    # print snakecase
    print('snake_case: ', end="")

    # loop through each letter
    for char in names:
    #  check if upper case
        if char.isupper():
    # print underscore and letter lower case
            print('_' + char.lower(), end='')
    # otherwise print letter
        else:
            print(char, end="")
main()
