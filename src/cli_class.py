class CommandLineInterface:
    def __init__(self):
        self.__display_banner()

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
        """

        print(ascii_art)


if __name__ == "__main__":
    command_line_interface = CommandLineInterface()
