import words
import hangman

allowed_errors = 6  # It should be 7 but the index of list is 0 not 1
missed_letters = []
correct_letters = []
finished = False

print("""
    Choices:
        C = countries
        A = animals
""")

category = input(f"Please enter the category: ")
if category == 'C':
    word = words.Country()
    category = 'Country'
elif category == 'A':
    word = words.Animals()
    category = 'Animals'
else:
    print('Not found')


while not finished:

    hangman.header(category, missed_letters)

    for letter in word:
        if letter.lower() in correct_letters:
            print(letter, end=' ')
        else:
            print('_', end=' ')
    print(' ')

    guess = hangman.getGuess(missed_letters + correct_letters)
    correct_letters.append(guess.lower())

    if guess.lower() not in word.lower():
        allowed_errors -= 1
        missed_letters.append(guess.lower())
        if allowed_errors == 0:
            hangman.header(category, missed_letters)
            print(f"No! The word was {word}")
            break

    finished = True

    for letter in word:
        if letter.lower() not in correct_letters:
            finished = False

if finished:
    hangman.header(category, missed_letters)
    print(f"You have guessed the word! It was {word}")
