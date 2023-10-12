def main():
    answer = input("What is the answer to the ultimate question of life, the Universe, and Everything? ")
    right_answer = ["42", "forty-two", "forty two"]

    if answer in right_answer:
        return "Yes"
    else:
        return "No"

print(main())