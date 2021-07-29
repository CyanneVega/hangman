def man(line):
    pics = ["  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",

            "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",

            "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",

            "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",

            "  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========",

            "  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========",

            "  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n========="]

    return pics[line]


def header(category, missed_letters):
    print("""
        HANGMAN
    """)
    print(man(len(missed_letters)))
    print('Category: ' + category)
    print('Missed Letters: ' + ' '.join(missed_letters))
    print('')


def getGuess(guessedWords):
    while True:
        guess = input(f"Guess a letter: ")
        print(' ')
        if len(guess.lower()) != 1:
            print('Enter a single letter')
        elif guess.lower() in guessedWords:
            print('You have already chosen the letter. Try again')
        elif guess.lower() not in 'abcdefghijklmnopqrstuvwxyz':
            print('Enter a letter')
        else:
            return guess.lower()
