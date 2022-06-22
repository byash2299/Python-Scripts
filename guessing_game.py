import sys
from random import randint

# Generate a number from 1 to 10
answer = randint(int(sys.argv[1]),int(sys.argv[2]))

# Get input from user

# Check if input is a number from 1 to 10

# Check if the number is a right guess. Ask again if wrong
while True:
    try:
        guess = int(input('Guess the number from 1 - 10  '))
        if 0 < guess <11:
            if answer == guess:
                print('Yeah, You guessed the right number')
                break
            else:
                print('Try again')
        else:
            print('Heyy, I said a number between 1 to 10')
    except ValueError:
        print('Please enter a number')
        continue


 