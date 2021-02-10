# Problem Set 2, hangman.py
# Name: Aditya Jadhav
# Description: Its a hangman game

# Hangman Game

import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


letters_guessed = []
letters_in_secret_word = []


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for characters in secret_word:
        if characters not in letters_guessed:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    i = 0
    answer = []
    q = 0
    while q < len(list(secret_word)):
        answer.append('_')
        q += 1
    for character in secret_word:
        if character in letters_guessed:
            answer[i] = secret_word[i]
        i += 1
    return ''.join(answer)


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''

    answer = list(string.ascii_lowercase)
    for letter in letters_guessed:
        answer.remove(letter)

    return ''.join(answer)


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''
    if len(my_word) != len(other_word):
        return False
    elif len(my_word) == len(other_word):
        i = 0
        while i < len(my_word):
            if list(my_word)[i] == list(other_word)[i] or list(my_word)[i] == '_':
                answer=True
                i+=1

            elif list(my_word)[i] != list(other_word)[i]:
                answer= False
                break
    return answer



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    list_of_words = []
    for other_word in wordlist:
        if match_with_gaps(my_word,other_word):
            list_of_words.append(other_word)

    return list_of_words


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    '''
    k = 0
    warning = 3

    while k < len(secret_word) and warning >= 0:
        print('You have', (len(secret_word) - k), 'guesses left')
        print('Available Letters: ', get_available_letters(letters_guessed))
        letter_input = input("Please guess a letter: ")
        if letter_input not in list(string.ascii_lowercase):
            print("Oops! That is not a valid letter. You have", warning, "warnings left: ",
                  get_guessed_word(secret_word, letters_guessed))
            warning -= 1
            k += 1
        elif letter_input in letters_guessed:
            print("Oops! You've already guessed that letter. You have", warning, " warnings left:",
                  get_guessed_word(secret_word, letters_guessed))
            warning -= 1
            k += 1
        elif letter_input not in list(secret_word):
            letters_guessed.append(letter_input)
            print("Oops! That letter is not in my word.")
            print("Please guess a letter:", get_guessed_word(secret_word, letters_guessed))
            print(show_possible_matches(get_guessed_word(secret_word, letters_guessed)))
            k += 1

        elif letter_input in list(secret_word):
            letters_guessed.append(letter_input)
            letters_in_secret_word.append(letter_input)
            print("Good guess:", get_guessed_word(secret_word, letters_guessed))
            print(show_possible_matches(get_guessed_word(secret_word, letters_guessed)))
            k += 1
            if is_word_guessed(secret_word, letters_guessed) == True:
                print("Congratulations, you won!")
                print("Your score: ", (len(secret_word) - k) * len(letters_in_secret_word))
                break

    if is_word_guessed(secret_word, letters_guessed) == False:
        print("Sorry, you ran out of guesses. The word was", secret_word)





if __name__ == "__main__":





    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)

