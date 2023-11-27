def main():
    # get input
    greeting = input('Greeting: ')
    # store the result of the value vunction
    value_to_print = value(greeting)
    print(f'${value_to_print}')

def value(greeting):
    # convertion
    greeting = greeting.lower().strip()
    # check if theres hello,h or neither
    if 'hello' in greeting:
        return 0
    elif 'h' == greeting[0]:
        return 20
    else:
        return 100

if __name__ == '__main__':
    main()