# importing emoji library
import emoji

def main():
    # asking for input
    emo = input('Input: ')

    # printing input as an emoji and added alias
    print(emoji.emojize(f'Output:{emo}', language='alias'))

main()