# Tic Tic Toe Game

### Tic tic toe is a python game, which runs in the terminal on Heroku.

### Two players can challenge each other. 'X' maintain first player roll and 'O' second. To win the match one of the player should complete a straight line of own letter in diagonal or horizontal or vertical.
### You can find my project Deploy here: https://tic-tac-toe-gpp3-76c82ce566fc.herokuapp.com/

![alt text](/images/tic-tac-toe1.png)

## How to play

### Tic-tac-toe game is based on the classic pen-paper game. You can read more about on wikipedia:-(https://en.wikipedia.org/wiki/Tic-tac-toe)

### This version is for two players, 
### 'X' is the first player turn and 'O' is the second player turn.
### The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row is the winner.

![alt text](/images/tic-tac-toe2.png)

## Features

### Existing features
    1. Two chances
       1. X's chance
       2. O's chance
![alt text](/images/Chances.png)

    2. Match over:
        1. X won the match or O won the match,
        2. Option to play again.
![alt text](/images/x-won-the-match.png)

### Input validation and Error checking
     1. The number within range 1-9,
     2. Option also chosen earlier,
     3. Accepts only numbers.

![alt text](/images/not-in-range.png)


## Future features
   1. Allow players to move in range 1-9
   2. Allow to play repetitively

## Data Model
  I decided to use a board formed nine empty places. It's much more easy to find out the way to win.


## Testing
I have manually tested this project by doing the following:
    1. Passed the code through a PEP8 linter and confirmed there are no problems.
    2. breake the game in case of typing n, no or other letters in the question of "Do you like to play again?"

## Solved Bugs

1. To find out the method for "Option also chosen earlier" (elif game_state[value - 1] is not None:), assisted by mentor.

## Remaining bugs



## Validator testing
  
1. PEP8
    No errors were found when passing through the PEP8online.com.

## Deployment
    
The live link can be found here - <https://tic-tac-toe-gpp3-76c82ce566fc.herokuapp.com/>


## Credits

1. Code institute for the deployment terminal.
2. Wikipedia for the details.
3. Code idea provided by <https://gist.github.com/CodeWithHarry/d83fed6958b7626ef51aa87c2d7130de>
    