# The game High and Low

from random import randint
guess_num = randint(1, 101)            # The range of random integers.
print("Here you can guess numbers between 1 and 100!")

for times_of_guesses in range(1, 11):
    guess = int(input(f'Guess {times_of_guesses}: '))   # the user enters

    if guess > guess_num:
        print('lower')
    elif guess < guess_num:
        print('higher')
    else:
        print(f'''Correct answer after only {times_of_guesses} guesses
        Excellent!''')
        exit(0)
print('You have tried 10 and the game is over')    # the range ends on 10 tries
