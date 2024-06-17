# Testing 

The following document outlines the testing protocols undertaken to ensure that all code was valid, as well as outlining any and all existing and solved bugs.

## Validation

### run.py 

Using the Code Institutes online Python Linter tool, to ensure that all code was PEP8 compliant. All code was validated upon first try, with the exception of line 7, where the code line was too long. This was fixed by continuing the code on a new line.

![Line 7 validation]()

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
