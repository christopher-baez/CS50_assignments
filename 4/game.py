import random

# loop to ask for lvl
while True:
    try:
        #ask for lvl
        lvl = int(input('Level: '))

        if lvl > 0:
            break
        else:
            continue
    except ValueError:
        continue

# generate number 1 - lvl
rand_num = random.randint(1, lvl)

# another loop to ask for guess
while True:
    try:
        # ask for guess
        guess = int(input('Guess: '))

        if guess > 0:
            if guess < rand_num:
                print('Too small')
                continue
            elif guess > rand_num:
                print('Too large!')
                continue
            else:
                print('just right!')
                break
    except ValueError:
        continue
    else:
        continue



