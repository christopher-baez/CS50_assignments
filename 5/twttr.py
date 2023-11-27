def main():
    word = input('input: ').lower()
    print(f'Output: {shorten(word)}')

def shorten(word):
    vowels = list('aeiou')
    result = ''
    for x in word:
        if x not in vowels:
            result += x
    return result





if __name__ == "__main__":
    main()