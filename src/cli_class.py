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

    def __display_menu_options(self):
        print("Menu Options")
        print("------------")
        print("1 - Local Multiplayer")
        print("2 - Single player")
        print("3 - Quit")


if __name__ == "__main__":
    command_line_interface = CommandLineInterface()
