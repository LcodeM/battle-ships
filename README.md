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

One game start, and after each previous guess while the user still has turns, or there are battleships remaining, the user is prompted to input first a row, then a column input between 1 and 8 and A and H, respectively. Failure to do so will lead to a ValueError and error message being printed. User is then prompted to input a correct value.

#### User Feedback messages

![Already guessed](https://github.com/LcodeM/battle-ships/blob/main/documentation/already_guessed_message.png)
The already guessed user feedback message let's the user know they have already guessed those coordinates, which are marked with a '-' on the board, as per the instructions at the beginning of the game. 

![Hit](https://github.com/LcodeM/battle-ships/blob/main/documentation/hit_message.png)
The hit message let's the user know their guess was correct, and they successfully sank a battleship. The board is then marked with an 'X'.

![Miss](https://github.com/LcodeM/battle-ships/blob/main/documentation/miss_message.png)
The miss message let's the user know their guess was incorrect, and they failed to hit a battelship. One turn is deducted, and the board is marked with a '-'.

![Error](https://github.com/LcodeM/battle-ships/blob/main/documentation/error_message.png)
Upon entering an incorrect value to the input for row or column, the user is given an Error message to indicate which value they need to input. Failure to do so will lead to a repeat of the error message.

#### End Game messages

![Game over](https://github.com/LcodeM/battle-ships/blob/main/documentation/game_over_message.png)
If the user runs out of turns, the game is over and game over message printed. 

![Win](https://github.com/LcodeM/battle-ships/blob/main/documentation/congratulations_message.png)
If the user hits all ships, congratulations message is shown.

In both instances, the restart_game function will then prompt the user to play again or quit.


### Future Features and Improvements to be Implemented

If I had more time, some future features that would be a good addition to the game would be:

- Add functionality for plotting own battleships and computer to randomly generate guesses for opponent.
- Add functionality for instructions to be a separate menu at the start of the game, or accessible at any time.
- Add functionality to show the number of remaining battleships before/after each turn.
- Add formatting of 'X' marker for hits as red.
- Add functionality to to quit the game during play.
- Add functionality for user to choose difficulty, introduce increase number of turns, fewer cpu ships to hit for EASY. Fewer turns, more ships for HARD, for example. 

## Flowchart

![Flowchart](https://github.com/LcodeM/battle-ships/blob/main/documentation/flowchart_logic.png)
The flowchart represents the logic of the application, and the steps taken in each instance when an input is prompted and/or made.

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

Render was chosen over Heroku, as Heroku no longer offers a free plan.

In order to successfully deploy to Render, user can follow the below steps:

- Step 1: Create a new account on [Render](https://render.com/) if you don't already have one.

- Step 2: Select New at the top of the page, and select Web Service
![Select web service](https://github.com/LcodeM/battle-ships/blob/main/documentation/create_web_service.png)

- Step 3: Select build from Github
![Deploy from github](https://github.com/LcodeM/battle-ships/blob/main/documentation/deploy_from_github_repo.png)

- Step 4: Connect your Github repository
![Repo select](https://github.com/LcodeM/battle-ships/blob/main/documentation/connect_repo.png)

- Step 5: Choose a name, region and branch for your project
![Name and branch](https://github.com/LcodeM/battle-ships/blob/main/documentation/select_name_region_branch.png)

- Step 6: Select free plan
![Free plan](https://github.com/LcodeM/battle-ships/blob/main/documentation/select_free_plan.png)

- Step 7: Set Environment Variable to PORT 8000
![Environment variable](https://github.com/LcodeM/battle-ships/blob/main/documentation/environment_variables.png)

- Step  8: Enter secret/ignored files for privacy of data, if required.
![Hidden files](https://github.com/LcodeM/battle-ships/blob/main/documentation/secret_files.png)

- Step 9: Build web service, then go to settings on the left hand side. Add build command ```pip install - r requirements && npm install```

- Step 10: Add start command ```node index.js```

- Step 11: Save changes and wait for deploy completion.

### Create a local clone

To create a local copy of this repository:
- First ensure you have Python installed on your computer. Enter ```install python3``` into your terminal.
- Secondly, ensure you also install other python packages. Enter ```get-pip.py``` into your terminal.
- Copy and paste https://github.com/LcodeM/battle-ships.git into your IDE workspace, or use ```git clone https://github.com/LcodeM/battle-ships.git ``` in your terminal.

## Testing

See [TESTING.md](https://github.com/LcodeM/battle-ships/blob/main/TESTING.md).

## Credits

- [Kaggle](https://www.kaggle.com/discussions/general/273188): Used to set text style in python (bright green)

- [Knowledge Mavens Youtube](https://www.youtube.com/watch?v=tF1WRCrd_HQ&ab_channel=KnowledgeMavens):
 Used as inspiration for creating classic battleships game
Original code: 
```py
For row in board:
	print(“%d|%s|” % (row_number, “|”.join(row)))
```
Simplified using [Phind.com](https://www.phind.com/search?home=true):
```py
For row in board:
	print(f”{row_number}|{‘|’.join(row)}|”)
```

- [Phind.com](https://www.phind.com/search?home=true): Troubleshooting and explaining code snippet functionality without offering direct solutions.

- [ioflood.com blog](https://ioflood.com/blog/randint-python/#:~:text=In%20this%20example%2C%20import%20random,number%20%2C%20which%20is%20printed%20out):
Support for importing ranint from random

- [The Hello World Program](https://thehelloworldprogram.com/python/python-string-methods/#:~:text=upper()%20method%20on%20a,thereof%20one%20must%20be%20silent): For .upper() function line 78.

- [Convert CSV to Markup](https://www.convertcsv.com/csv-to-markdown.htm) Used to convert CSV of manual testing to markup table.

- [docs.Render](https://docs.render.com/node-version) Setting Node for deployment

- [Iuliia Konovalova - Mentor](https://github.com/IuliiaKonovalova/madlib_with_python/blob/main/README.md) Support with deployment instrucions to Render.com