class Hangman:
    def __init__(self, word_to_guess):
        self.__word_to_guess = word_to_guess
        self.__guesses_remaining = 7
        self.__letters_guessed = []
