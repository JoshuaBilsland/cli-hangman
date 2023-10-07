from random_words import RandomWords
import hangman_class


class CommandLineInterface:
    def __init__(self):
        self.__display_banner()
        self.__main_menu()

    def __display_banner(self):
        ascii_art = """
         _                                             
        | |                                            
        | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
        | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \  
        | | | | (_| | | | | (_| | | | | | | (_| | | | |
        |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                            __/ |                      
                           |___/
        """  # noqa: E701, W605, W291

        print(ascii_art)

    def __main_menu(self):
        self.__display_menu_options()

        running = True
        while running:
            choice = input(
                "Enter the number of the menu option you want to select >> "
            )
            if choice == "1":
                word = self.__player_choose_word()
            elif choice == "2":
                user_word_len = self.__player_choose_word_len()
                word = self.__generate_random_word(word_len=user_word_len)
            elif choice == "3":
                running = False
            else:
                print("Invalid menu option")

            if choice in ["1", "2"]:
                self.__game_loop(hangman_class.Hangman(word))
                self.__display_menu_options()

    def __display_menu_options(self):
        print("\nMenu Options")
        print("------------")
        print("1 - Local Multiplayer")
        print("2 - Single player")
        print("3 - Quit")

    def __player_choose_word(self):
        # If multiplayer is chosen,
        # let one player enter the word for the other to guess.

        valid_word = False
        while not valid_word:
            user_word = input("Enter a word for the other player to guess >> ")
            if not user_word.isalpha() or len(user_word) < 2:
                print("ERROR: Invalid Word. Word must only contain letters and"
                      "be at least two characters in length")
            else:
                valid_word = True

                # Print blank lines to hide the
                for line in range(100):
                    print()

                return user_word

    def __player_choose_word_len(self):
        validInput = False
        while not validInput:
            try:
                user_word_len = int(input("Enter the number of letters you "
                                          "want the word to guess to contain "
                                          ">> "))
            except ValueError:
                print("ERROR: Only enter a number")
            else:
                validInput = True
        return user_word_len

    def __generate_random_word(self, word_len=None):
        rw = RandomWords()
        if word_len is None:
            word = rw.random_word()
        else:
            # random_words package only lets you set the min letter count
            # and so keep generating words until one is the right length
            word = rw.random_word(min_letter_count=word_len)
            while len(word) != word_len:
                word = rw.random_word(min_letter_count=word_len)
        return word

    def __game_loop(self, hangman_game):
        while (hangman_game.get_guesses_remaining() != 0 and
               not hangman_game.is_word_guessed()):
            print("-----------------")
            print(hangman_game.get_current_stage())
            print("Guesses Remaining:", hangman_game.get_guesses_remaining())
            print()
            print("Word To Guess:", hangman_game.get_hidden_word())
            user_guess = input("Guess a letter >> ")

            result = hangman_game.check_user_guess(user_guess)
            if result == "INVALID_GUESS":
                print("ERROR: Invalid Guess. Guess must be a single letter")
            elif result == "LETTER_ALREADY_GUESSED":
                print("ERROR: Letter already guessed. Guess a different letter"
                      )
            elif result == "CORRECT_GUESS":
                print("Correct guess!")
            elif result == "INCORRECT_GUESS":
                print("Incorrect guess!")
        if hangman_game.get_guesses_remaining() == 0:
            print("You lose! You ran out of guesses")
            print("The word was", hangman_game.get_word_to_guess())
        elif hangman_game.is_word_guessed():
            print("")


if __name__ == "__main__":
    command_line_interface = CommandLineInterface()
