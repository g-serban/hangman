import random
from words import list_of_words
import string


def get_valid_words(words):
    selected_word = random.choice(words)
    while '-' in selected_word or ' ' in selected_word:   # because we have some nouns with - and spaces, we need to iterate to the next word 
        selected_word = random.choice(words)

    return selected_word.upper()


def hangman():
    word = get_valid_words(list_of_words)
    word_letters = set(word)    # here we track the letters in the word
    alphabet = set(string.ascii_uppercase)
    letters = set()   # here we track what uppercase letters the user has guessed 
    lives = 6

    # getting user input
    while len(word_letters) > 0 and lives >= 1:
        # letters used
        print('You have', lives, 'left and you have used these letters: ', ' '.join(letters))

        # what the current word is but with dashes for where the user hasn't guessed yet
        word_list = [letter if letter in letters else '-' for letter in word]
        print('Current word is: ', ' '.join(word_list))

        user_input = input('Guess a letter: ').upper()
        if user_input in alphabet - letters:      # if the input is in the alphabet + is not in letters, then add it to letters set
            letters.add(user_input)
            if user_input in word_letters:
                word_letters.remove(user_input)
            else:
                lives = lives - 1  # takes away a life if wrong
        elif user_input in letters:
            print('You already guessed that letter before!')
            continue
        else:
            print('Invalid character. Please try again!')
            continue
    # gets here when 1. user guesses all the words or 2. no lives left
    if lives == 0:
        print('You have died!! The word was', word)
    else:
        print('You guessed the', word, 'correctly. Congrats!!')
    play_again = input('Wanna play again? (Yes/No): ').lower()
    if play_again == 'yes':
        hangman()
    else:
        print('Thank you for playing the game!')
        

hangman()









