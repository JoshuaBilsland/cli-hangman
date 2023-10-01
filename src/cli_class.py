from random_words import RandomWords


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
                self.__player_choose_word()
            elif choice == "2":
                user_word_len = self.__player_choose_word_len()
                print(self.__generate_random_word(word_len=user_word_len))
            elif choice == "3":
                running = False
            else:
                print("Invalid menu option")

    def __display_menu_options(self):
        print("Menu Options")
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


if __name__ == "__main__":
    command_line_interface = CommandLineInterface()
