# Battleships

## Introduction

Battleships is a python terminal game, aimed at users who are looking for a quick challenge in the form of the classic battleships game.

The link to the game can be found [here](https://battle-ships-69q8.onrender.com/).

## How to play

Upon page load:
- If the game does not start automatically, click Run Program at the top of the page.
- Read the welcome message and instructions.
- Input a value for row between 1 and 8.
- Input a value for column between A and H.
- Repeat until:
    - All 5 battleships hit
    - Out of lives
- Once game over, press y to restart or n to quit.

## User Stories

### First Time User Goals

- As a first time user, I want to immediately be able to understand the purpose of the game, and how to play.
- As a first time user, I want the game to be visually appealing and easy to see.
- As a first time user, I want the game to be easy to play with minimum input
- As a first time user, I want to be updated with my progress through the game.
- As a first time user, I want to have the option to replay the game once it is over.

## Features

### Existing Features

#### Welcome message and instructions

![Welcome](https://github.com/LcodeM/battle-ships/blob/main/documentation/welcome_message.png)

Upon game load, the user is presented with a welcome message and instructions on how to play the game. 

Note that these instructions are only printed upon game start/restart.

#### Player board

![Player Board](https://github.com/LcodeM/battle-ships/blob/main/documentation/player_board.png)

Upon start, the player board is generated as blank, using an x and y axis with numbers and letters for the rows and columns respectively.

The board is updated and regenerated with the users guesses after both row and column have been inputted, with either a '-' for a miss, or an 'X' for a hit.

#### CPU board

![CPU Board](https://github.com/LcodeM/battle-ships/blob/main/documentation/cpu_board.png)

The CPU board is hidden, as to provide the challenge of not knowing where the battleships are located. But if called upon, looks like the above, with the battelships identified as 'O'.

#### Player input

![Player input](https://github.com/LcodeM/battle-ships/blob/main/documentation/user_input.png)

#### User Feedback messages

![Already guessed](https://github.com/LcodeM/battle-ships/blob/main/documentation/already_guessed_message.png)
![Hit](https://github.com/LcodeM/battle-ships/blob/main/documentation/hit_message.png)
![Miss](https://github.com/LcodeM/battle-ships/blob/main/documentation/miss_message.png)
![Error](https://github.com/LcodeM/battle-ships/blob/main/documentation/error_message.png)

#### End Game messages

![Game over](https://github.com/LcodeM/battle-ships/blob/main/documentation/game_over_message.png)

### Future Features and Improvements to be Implemented

If I had more time, some future features that would be a good addition to the game would be:

- Add functionality for plotting own battleships and computer to randomly generate guesses for opponent.
- Add functionality for instructions to be a separate menu at the start of the game, or accessible at any time.
- Add functionality to show the number of remaining battleships before/after each turn.
- Add formatting of 'X' marker for hits as red.
- Add functionality to to quit the game during play.

## Technologies

### Languages

The list of technologies used for completion of the site are as follows:

- [Python 3.12](https://www.python.org/) - used to write all code for the project and determine function of web app.
- [Git](https://git-scm.com) - used to track changes in code and version control.

### Libraries

#### Standard Library imports:

- [random](https://docs.python.org/3/library/random.html) - used to generate random numbers for cpu battleships on cpu board.

### Other Tools

- [Github]() - used as repository host.
- [VSCode](https://code.visualstudio.com/) - used to set up workspaces and main tool for writing/editing of code.
- [Render](https://render.com/) - used as an alternative to Heroku, as it provides a free service.


## Deployment

### Deploying to Render



## Testing

See [TESTING.md]().

## Credits

