import os


class Hangman:
    def __init__(self, word_to_guess):
        self.__word_to_guess = word_to_guess
        self.__max_guesses = 7
        self.__guesses_remaining = self.__max_guesses
        self.__letters_guessed = []

    # Getters
    def get_word_to_guess(self):
        return self.__word_to_guess

    def get_guesses_remaining(self):
        return self.__guesses_remaining

    def get_letters_guessed(self):
        return self.__letters_guessed

    # Other
    def get_current_stage(self):
        # 8 is the number of 'stage' files
        guesses_per_stage = self.__max_guesses / 8
        stage_to_display = int((self.__max_guesses - self.__guesses_remaining)
                               / guesses_per_stage)
        stage_to_display = max(0, min(stage_to_display, 8 - 1))

        # Create the full path to the ascii_art text file
        stage_filename = f"stage{stage_to_display}.txt"
        full_path = os.path.join("res", "hangman_stages", stage_filename)

        with open(full_path, "r") as stage_file:
            ascii_art = stage_file.read()

        return ascii_art

    def get_hidden_word(self):
        hidden_word = ""
        for letter in self.__word_to_guess:
            if letter in self.__letters_guessed:
                hidden_word += letter
            else:
                hidden_word += "_"
        return hidden_word

    def check_user_guess(self, user_guess):
        if len(user_guess) != 1 or not user_guess.isalpha():
            result = "INVALID_GUESS"
        elif user_guess in self.__letters_guessed:
            result = "LETTER_ALREADY_GUESSED"
        elif user_guess in self.__word_to_guess:
            result = "CORRECT_GUESS"
            self.__letters_guessed.append(user_guess)
        else:
            result = "INCORRECT_GUESS"
            self.__guesses_remaining -= 1
        return result

    def is_word_guessed(self):
        # Check if all the letters of the word have been guessed
        for letter in self.__word_to_guess:
            if letter not in self.__letters_guessed:
                return False
        return True
