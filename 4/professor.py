import random

def get_level():
    # loop to get level, the higher the lvl the harder questions get
    while True:
        level = int(input('Level: '))
        if level == 1:
            return 10
        elif level == 2:
            return 100
        elif level == 3:
            return 1000
        else:
            continue

def generate_integer(level):
    # function to generate random integer
    return random.randint(1, level)

def main():
    # variable taken from get_level
    level = get_level()
    # empty variable to keep score
    score = 0
    # ask 10 questions
    for q in range(10):
        x = generate_integer(level)
        y = generate_integer(level)

        # empty variable for attempts count
        attempts = 0
        # making false statement to use to move to next questions
        correct = False
        # while loop as long as attempts under 3
        while attempts < 3 and not correct:
            try:
                # format for questions
                answer = int(input(f'{x} + {y} = '))
                # check if answer correct
                if answer == x + y:
                    correct = True
                    if attempts == 0:
                        score += 1  # increment score if the first attempt is correct
                else:
                    print('EEE')
                    attempts += 1

                if attempts == 3:
                    print(f"{y} + {x} = {x+y}")
            except ValueError:
                continue
    # Display the final score
    print(f"score: {score}")

if __name__ == "__main__":
    main()
