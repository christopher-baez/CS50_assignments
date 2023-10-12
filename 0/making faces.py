
#string modifier
def convert(text):
    mod_str = text.replace(':)', '🙂').replace(":(", "🙁")
    print(mod_str)
#main function
def main():
    user_input = input("Please enter your text:")
    converted_text = convert(user_input)
    print(convert)
main()

