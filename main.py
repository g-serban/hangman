import random
from words import list_of_words
import string


def get_valid_words(words):
    selected_word = random.choice(words)

    while '-' in selected_word or ' ':   # because we have some nouns with - and spaces, we need to iterate to the next word 
        selected_word = random.choice(words)

    return selected_word.upper()


def hangman():
    word = get_valid_words(list_of_words)
    word_letter = set(word)    # here we track the letters in the word
    alphabet = set(string.ascii_uppercase)
    letters = set()   # here we track what uppercase letters the user has guessed 
    user_input = set(input('Guess a letter: '))   
    if user_input in alphabet - letters:      # if the input is in the alphabet, then add it to used_letters set
        letters.add(user_input)
        if user_input in word_letter:
            word_letter.remove(user_input)
    elif









