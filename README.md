![Project banner](res/banner.png)

<div align="center">
    <img alt="GitHub last commit (branch)" src="https://img.shields.io/github/last-commit/JoshuaBilsland/cli-hangman/main">
    <img alt="GitHub issues" src="https://img.shields.io/github/issues/JoshuaBilsland/cli-hangman">
    <img alt="GitHub top language" src="https://img.shields.io/github/languages/top/JoshuaBilsland/cli-hangman">
    <p>A command-line hangman game.</p>
</div>



![Gif showing a demo of the program](res/demo.gif)

# Table of Contents

- [Installation Guide](#installation-guide)
- [Usage Guide](#usage-guide)
  - [Local Multiplayer](#local-multiplayer)
  - [Single Player](#single-player)
- [Configuration Guide](#configuration-guide)
  - [Changing the Number of Guesses](#changing-the-number-of-guesses)
- [Project Purpose and Aims](#project-purpose-and-aims)
- [And Now for Something Completely Different, Post-Project Evaluation and Next Steps](#and-now-for-something-completely-different-post-project-evaluation-and-next-steps)
  - [Project Successes](#project-successes)
  - [Room for Improvement](#room-for-improvement)
  - [Next Steps](#next-steps)

# Installation Guide
1. Clone this repository
```
git clone https://github.com/JoshuaBilsland/cli-hangman.git
```
2. Go into the repository
```
cd cli-hangman
```
3. [Create Python virtual environment](https://youtu.be/KxvKCSwlUv8)
4. Install dependencies
```
pip install -r requirements.txt
```
5. Run `cli_class.py`
   
# Usage Guide
The program has two game modes  
![Image showing the main menu](res/usage_guide_menu_options.png)
## Local Multiplayer
If option `1` is selected on the main menu then local multiplayer will be selected. In this mode, one player can type in a word for the other player to guess.  
![Image showing local multiplayer be selected](res/usage_guide_local_multiplayer.png)
## Single Player
If option `2` is selected on the main menu then single player will be selected. In this mode, the player enters how long of a word they want to guess. A word of that length will then be generated for them to guess.  
![Image showing single player be selected](res/usage_guide_single_player.png)

# Configuration Guide
## Changing the Number of Guesses
The `Hangman` class has been designed so that the `max_guesses` variable can be increased or decreased to make the game easier or more difficult. The `get_current_stage` method is able to 'evenly' distribute the ASCII art stage files so that the drawing of the hangman is updated in a way that is balanced with `max_guesses`. For example, if you double the number of `max_guesses`, from 7 to 14, rather than display one stage per incorrect guess, instead the next stage will be displayed after every two incorrect guesses.

To change `max_guesses`, go to the `hangman_class.py` file in the `src` folder. Go to the constructor of the class and edit the value of `self.__max_guesses`.

```
# The Hangman constructor

class Hangman:
    def __init__(self, word_to_guess):
        self.__word_to_guess = word_to_guess
        self.__max_guesses = 7  # <--------------------------- Change this 7
        self.__guesses_remaining = self.__max_guesses
        self.__letters_guessed = []
```

# Project Purpose and Aims
The main reason for creating this project is to improve my knowledge of conventions and getting into the habit of following them. I eventually want to try and get a degree apprenticeship in software development, and by learning industry conventions, it may improve my chances of getting one as well as making it easier for me to start working with a team of developers if I manage to get one. My previous projects did not really follow any industry conventions (although I was to some extent following my own that I had naturally started doing and what I had been taught at GCSEs and A-levels). Below is a list summarising the conventions I want to follow.

- Python Convention - PEP8 (https://peps.python.org/pep-0008/)
- Git Commit Message Convention - Conventional Commits (https://www.conventionalcommits.org/en/v1.0.0/)
- README Template - (https://github.com/JoshuaBilsland/my-conventions) 

For more information please see https://github.com/JoshuaBilsland/my-conventions.

# And Now for Something Completely Different, Post-Project Evaluation and Next Steps
Now that my project is complete (other than a few sprinkles), I want to use this section to write out an evaluation of my project when compared to the ["Project Purpose and Aims" section](#project-purpose-and-aims) as well as talk about what I am planning to learn/do next. 
## Project Successes
Overall, this project has been successful. The main purpose of this project was to improve my knowledge of conventions (PEP8, 'Conventional Commits', and README layouts), and I believe I have done this. Although I still need to refer back to them occasionally, particularly PEP8, I do feel much more confident with them. On top of that, I now have a Hangman project! 🎉. As a bonus, I found myself starting to look into conventional ways of laying out a repository (what folders to use, what to call them, where different files belong, etc). I did not set out to do this (just yet) but it has been useful to start doing this.
## Room for Improvement
As I said in the previous section, I still find myself needing to refer back to the conventions occasionally, particularly when it comes to PEP8, as there is a lot to learn, so one area for improvement is to keep using these conventions (which I plan to do anyway) until they become second nature. I also mentioned in the previous section that I started looking into repository structure conventions, which I didn't intend to do for this project. I feel this was a mistake, and I should have looked into it along with the other conventions rather than planning to leave it to a separate project (which I was going to do by creating a project that would involve many files and folders so that I could really focus on a good structure). A final area for improvement is when it comes to committing. I now feel pretty confident with writing 'Conventional Commits', but I still feel I am struggling to identify WHEN to commit. With all that said...
## Next Steps
- Practice with PEP8
- Learning and practicing repository structure
- Get better at identifying when I should be committing
- Learning how to use Git branches
- Learning good software design
- I am currently reading through "The Pragmatic Programmer" which talks about good programming practices and software design. My next big focus is to go further with this and learn much more about good software design and writing better code (in terms of principles to follow, breaking things down into multiple functions, how to separate code into different files, etc).