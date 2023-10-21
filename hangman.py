import random
import string
from words import words

def get_valid_word():
    word = random.choice(words)

    while ' ' in word or '-' in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = get_valid_word()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print(f'You have  {lives} lives left.You have used these characters.',' '.join(used_letters))

        word_list =[letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Enter letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print('Letter not in word')
        elif user_letter in used_letters:
            print('You have already used that letter.Try again')
        else:
            print('Invalid character.Try again')

    if lives == 0:
        print('Sorry.You died!!! The word is', word)
    else:
        print('Congratulations. You guessed the word correctly as',word)

hangman()