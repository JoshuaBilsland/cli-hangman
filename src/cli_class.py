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
                print(2)
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
        """
        If multiplayer is chosen,
        let one player enter the word for the other to guess.
        """
        valid_word = False
        while not valid_word:
            user_word = input("Enter a word for the other player to guess >> ")
            if not user_word.isalpha() or len(user_word) < 2:
                print("ERROR: Invalid Word. Word must only contain letters and"
                      "be at least two characters in length")
            else:
                valid_word = True
                return user_word


if __name__ == "__main__":
    command_line_interface = CommandLineInterface()
