def main():
    # ask for input
    text = input("Input: ")
    # convert input to lowercase
    new_text = text.lower()
    # blank varable to store result
    result = ''
    # remove all vowels
    vowels = 'aeiou'
    for x in new_text:
        if x not in vowels:
            result += x
    print(f'Output: {result}')

main()




