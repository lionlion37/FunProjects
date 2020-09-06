import os
import sys
import random
import codecs
from hangman_utils import screen, validate_input

errors = 0
round = 0
stage_id = 0
win = False
valid = False
guesses = []

# Introduction screen --------------------------------------------------------------------------------------------------

os.system('clear')
os.system('figlet hangman')
print('\n\n')
print('\n############### Instructions ###############\n')
print('1. Choose a random word. Make sure your playing partner can\'t see your choice! If you play alone, you can '
      'also let the computer choose a random word from either english or german for you.\n\n'
      '2. You have to guess the given word by guessing its letters. If the word contains the '
      'guessed letter, it will be filled out. If not, hangman will come one step closer to getting hung!\n')
print('############################################\n\n')

# generate or self set?
while not valid:
    generate = str(input('Do you want to get a randomly generated word? Type "y" for yes or "n" for no: '))

    if generate == 'y':
        lan_valid = False

        while not lan_valid:
            language = str(input('Choose a language. Type "en" for english or "de" for german: '))

            if language not in ['en', 'de']:
                print('Invalid input! Try again.\n')
                continue

            lan_valid = True

            # read chosen language file and randomly choose a word
            f = codecs.open(os.path.join('word_data', language + '.txt'), "r", 'iso-8859-15')
            words = f.readlines()
            word = random.choice(words)
            word = str(word).strip('[]')
            word = str(word).strip("''")
            word = str(word).strip("\n")
            word = str(word).strip("\r")
            word = word.lower()

        valid = True

    elif generate == 'n':
        while not valid:

            # get a custom word
            word = str(input('Enter your world: '))
            valid, word = validate_input(word)
            if not valid:
                print('You can\'t use this word! Please try again.\n')

        valid = True

    else:
        print('Invalid input! Try again.\n')
        continue

word_str = '_ ' * len(word)
os.system('clear')

# Guessing screen ------------------------------------------------------------------------------------------------------

screen(word_str, stage_id, '')

while stage_id < 10:

    guesses_str = ''

    # validate guess
    valid_guess = False
    while not valid_guess:
        guess = str(input('Guess a character: '))
        valid_guess, _ = validate_input(guess)

        if not valid_guess or len(guess) != 1 or guess == ' ':
            print('You\'ve made an invalid guess! Please try again.\n')
            valid_guess = False

        if guess in guesses:
            print('You\'ve already guessed that! Try again.\n')
            valid_guess = False

    guesses.append(guess)

    # update word string if guessed character is in word
    if guess in word:
        ids = []
        word_str = ''
        for n, letter in enumerate(word):
            if letter in guesses:
                word_str = word_str + letter + ' '
            else:
                word_str = word_str + '_ '

        # check if whole word has been already guessed
        if '_' not in word_str:
            win = True
            os.system('clear')
            screen(word_str, stage_id, guesses_str)
            round += 1
            break

    # update stage if guessed wrong
    else:
        stage_id += 1
        errors += 1

    # generate guess string to display already taken guesses
    try:
        for n, g in enumerate(guesses):
            if n != len(guesses) - 1:
                guesses_str = guesses_str + str(g) + ', '
            else:
                guesses_str = guesses_str + str(g)

    except Exception as e:
        pass

    os.system('clear')
    screen(word_str, stage_id, guesses_str)
    round += 1

# finish screen --------------------------------------------------------------------------------------------------------

# win screen
if win:
    os.system('figlet congrats!')
    print(f'\nYou\'ve beaten the game after {round} rounds and with {errors} wrong guesses!\n')

# loose screen
else:
    os.system('clear')
    os.system('figlet ":-("')
    print('\nYou\'ve lost...\n')

    # show the word?
    show_word = str(input('Do you want to show the word? Type "y" for yes or "n" for no: '))

    # only do something if 'yes' was chosen
    if show_word == 'y':
        print("\nThe word is:\n")
        os.system(f'figlet {word}')

# try again?
try_again = str(input('\nWant to try again? Type "y" for yes or "n" for no: '))
if try_again == 'y':
    os.execl(sys.executable, sys.executable, *sys.argv)

elif try_again == 'n':
    print('\nSad to see you go!\n')

else:
    print('\nFalse input! Assuming you want to stop the program. Bye Bye!')
