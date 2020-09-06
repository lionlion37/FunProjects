import os

def stages(stage: int):
    """storage function for different hang stages"""
    if stage == 0:
        print('___________________________')

    elif stage == 1:
        for _ in range(10):
            print(' ')
        print('         _________ ')
        print('       _/         \_')
        print('     _/             \_')
        print('____/_________________\____')

    elif stage == 2:
        print(' ')
        print('             |')
        print('             |')
        print('             |')
        print('             |')
        print('             |')
        print('             |')
        print('             |')
        print('             |')
        print('             |')
        print('         _________ ')
        print('       _/         \_')
        print('     _/             \_')
        print('____/_________________\____')

    elif stage == 3:
        print('             ______________')
        print('             |             ')
        print('             |')
        print('             |')
        print('             |')
        print('             |')
        print('             |')
        print('             |')
        print('             |')
        print('             |')
        print('         _________ ')
        print('       _/         \_')
        print('     _/             \_')
        print('____/_________________\____')

    elif stage == 4:
        print('             ______________')
        print('             |             |')
        print('             |')
        print('             |')
        print('             |')
        print('             |')
        print('             |')
        print('             |')
        print('             |')
        print('             |')
        print('         _________ ')
        print('       _/         \_')
        print('     _/             \_')
        print('____/_________________\____')

    elif stage == 5:
        print('             ______________')
        print('             |             |')
        print('             |             |')
        print('             |             O')
        print('             |')
        print('             |')
        print('             |')
        print('             |')
        print('             |')
        print('             |')
        print('         _________ ')
        print('       _/         \_')
        print('     _/             \_')
        print('____/_________________\____')

    elif stage == 6:
        print('             ______________')
        print('             |             |')
        print('             |             |')
        print('             |             O')
        print('             |             |')
        print('             |')
        print('             |')
        print('             |')
        print('             |')
        print('             |')
        print('         _________ ')
        print('       _/         \_')
        print('     _/             \_')
        print('____/_________________\____')

    elif stage == 7:
        print('             ______________')
        print('             |             |')
        print('             |             |')
        print('             |             O')
        print('             |            \|/')
        print('             |')
        print('             |')
        print('             |')
        print('             |')
        print('             |')
        print('         _________ ')
        print('       _/         \_')
        print('     _/             \_')
        print('____/_________________\____')

    elif stage == 8:
        print('             ______________')
        print('             |             |')
        print('             |             |')
        print('             |             O')
        print('             |            \|/')
        print('             |             |')
        print('             |')
        print('             |')
        print('             |')
        print('             |')
        print('         _________ ')
        print('       _/         \_')
        print('     _/             \_')
        print('____/_________________\____')

    elif stage == 9:
        print('             ______________')
        print('             |             |')
        print('             |             |')
        print('             |             O')
        print('             |            \|/')
        print('             |             |')
        print('             |             /\ ')
        print('             |')
        print('             |')
        print('             |')
        print('         _________ ')
        print('       _/         \_')
        print('     _/             \_')
        print('____/_________________\____')

    elif stage == 10:
        print('             ______________')
        print('             |             |')
        print('             |             |')
        print('             |             XX')
        print('             |            \|/')
        print('             |             |')
        print('             |             /\ ')
        print('             |')
        print('             |')
        print('             |')
        print('         _________ ')
        print('       _/         \_')
        print('     _/             \_')
        print('____/_________________\____')


def screen(word_str: str, stage_id: int, guesses_str: str):
    """display word string, hang stage and already taken guesses"""
    print('\n\n\n\n')
    # display word string
    os.system(f'figlet {word_str}')
    print('\n\n\n')

    # display hangman
    stages(stage_id)
    print('\n\n')

    # display guessed characters if there are any
    if guesses_str != '':
        print('Already guessed characters:\n')
        print(guesses_str)
        print('\n')
    else:
        print('\n\n')


def validate_input(inp: str):
    """check if input is a valid letter of the alphabet"""
    valid = True
    inp = inp.lower()

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z', 'ä', 'ö', 'ü', 'ß']

    # check if there even is an input
    if inp == '':
        valid = False

    # check for every letter if it's in the alphabet
    for letter in inp:
        if letter not in alphabet:
            valid = False

    return valid, inp
