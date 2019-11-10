# Snakes-and-Ladders
A Project for 15-112 @ CMU-Q

## Project Overview
This project aims to develop an online multiplayer game called Snakes & Ladder. The game (including the GUI) will be built from scratch using Python 3.7. 

### Description
Snakes & Ladders is an ancient Indian boardgame played widely today. The board has boxes numbered from 1 to 100. The game usually consists of atleast 2 players (but 4 players gameplay is common as well). These player get to choose unique colored tokens. The first person who reaches 100th box wins. Some boxes have ladders leading to higher numbered box (boosting the player's chances of winning) or have snakes leading back to the lowered number box (reducing the player's chances of winning). The dice is numbered from 1 to 6. With each 6 the player gets to roll the dice again. However, three consecutive sixes will cancel all the score for this particular 
###### A demo of the board can be found [here](http://toytheater.com/wp-content/uploads/snakes_and_ladders.gif).

### Components
1. Game Boards - multiple board designs  
2. Multiplay - allows human vs computer mode and multiplayer gameplay (for upto 4 players)
3. Dice - for players
4. Scoreboard - shows live scores and final scores at the end of the game
5. Online - allows both offline and online gameplay 
6. Animation - for the tokens and dice
7. Save Data - shows  most recent game scores (scoreboard) even after closing and reopening
8. Save Game - saves the game and allows resume 

### Implementation 
A high-level sketch of the game implementation is as follows. The game boards will be imported from web and displayed in a window using Tkinter. Mouse clicking functionality will be used to click the dice, which will generate a random number between 1 and 6. The tokens will be of different colors and will be generated as 'sprites' from the Tkinter library. To detect individual boxes on the board, OpenCV may be used. Snakes and ladders are special case boxes and so parent-child model of classes may be used to add such added-functionality to the block.

### Deliverables 
- For first checkpoint, components 1 to 4 are expected to be completed.
- For final checkpoint, componenets 5 to 8 are expected to be implemented. 

##### Libraries: Tkinter, Random, Socket, and Numpy will be used for the development. More libraries will be added later as necessary. 


