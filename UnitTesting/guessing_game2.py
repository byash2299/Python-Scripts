from random import randint

def run_guess(guess, answer):
    if 0 < guess <11:
        if answer == guess:
            print('Yeah, You guessed the right number')
            return True
        else:
            print('Try again')
    else:
        print('Heyy, I said a number between 1 to 10')
        return False

if __name__ == '__main__':
    answer = randint(1, 10)
    while True:
        try:
            guess = int(input('guess a number 1~10:  '))
            if (run_guess(guess, answer)):
                break
        except ValueError:
            print('please enter a number')
            continue
