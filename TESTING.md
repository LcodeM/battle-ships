# Testing 

The following document outlines the testing protocols undertaken to ensure that all code was valid, as well as outlining any and all existing and solved bugs.

## Validation

### run.py 

Using the Code Institutes online Python Linter tool, to ensure that all code was PEP8 compliant. All code was validated upon first try, with the exception of line 7, where the code line was too long. This was fixed by continuing the code on a new line.

![Line 7 validation](https://github.com/LcodeM/battle-ships/blob/main/documentation/validation_linter.png)

This issue then proceded to show an error of trailing white space in the linter, but this should not effect the function or performance of the program. 

## Manual Testing

|Page Feature           |Action(s)                                             |Expected result                                                                             |Tested|Passed/Failed|Comments                                                          |
|-----------------------|------------------------------------------------------|--------------------------------------------------------------------------------------------|------|-------------|------------------------------------------------------------------|
|Welcome                |Page load                                             |Welcome message, instructions and board displayed                                           |Yes   |Pass         |With free Render account, applications can take up to 50s to load.|
|Input row pass         |User input (row)                                      |User inputs correct value, Input column displayed                                           |Yes   |Pass         |                                                                  |
|Input row fail         |User input (row)                                      |User inputs incorrect value, ValueError message displayed                                   |Yes   |Pass         |                                                                  |
|Input column pass      |User input (column)                                   |User inputs correct value, hit/miss/already guessed message displayed                       |Yes   |Pass         |                                                                  |
|Input column fail      |User input (column)                                   |User inputs incorrect value, ValueError message displayed                                   |Yes   |Pass         |                                                                  |
|Already guessed message|User inputs same guess as before                      |Error message: Already guessed those coordinates, displayed                                 |Yes   |Pass         |                                                                  |
|Hit message            |User inputs correct guess                             |Hit message: That’s a hit! message, count incremented by 1                                  |Yes   |Pass         |                                                                  |
|Miss message           |User inputs incorrect guess                           |Miss message: Sorry, you missed… turns decremented by 1                                     |Yes   |Pass         |                                                                  |
|Run out of turns       |User has 0 turns left                                 |Game over message: Game over. You ran out of turns… restart_game function displayed         |Yes   |Pass         |                                                                  |
|All ships sunk         |User hits all 5 ships                                 |Congratulations message: Congrats, you sank all battleships! restart_game function displayed|Yes   |Pass         |                                                                  |
|Restart game           |Game ends, user selects Y or N, game restarts or ends.|User prompted with option to restart game “Y or N” choice                                   |Yes   |Pass         |                                                                  |
|Restart game fail      |User inputs invalid                                   |Error message: Please input a correct value                                                 |Yes   |Pass         |                                                                  |

## Bugs

### Solved Bugs

1: converting code from Knowledge Mavens to simpler code for printing rows with “|” as spacing. Used Phind to troubleshoot for more modern code, used concatenation with print(f” …) 

2: Random integer import not working. Fixed: import and from wrong way round, now using: from random import randint 
ref: ioflood blog

3: choose column/row function not working… Fix: Phind.com to troubleshoot, suggested using while loop for try:except function and create new function to run both inputs. 

4: column info still printing as row info but looking for string. Fix: edit print message to user.

5: place_cpu_battleships not working when run in terminal. Fix: line 41, missed second set of coordinates for column.

6: Testing hit/miss with if, elif, else statement… not registering 8 as valid row… Fix: missing 8 in list of numbers in if statement - line 56.

7: Testing hit/miss with if, elif, else statement… G registering as H… Fix: line 7, y-axis converter not using 0 indexing, shots registering 1 to the right.

8: Input invalid if user doesn’t input capital letter A-H… fix: (line 75) added .upper() to end of line of code.

9: After deploying and making changes, the win message doesn’t show and restart function isn’t called once user hits all 5 ships. Fix: Call count_hits function inside game loop. Line 160

### Ongoing bugs

1: When selecting the same coordinates of a hit battleship, current message still shows "hit". This doesn't cause any problems, as the game does not register an additional hit or miss, nor does it decrement a turn. In the future with more time, fixing this to prompt the same 'already guessed' message would be more suitable. 