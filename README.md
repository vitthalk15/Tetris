##OOPS project

#Tetris Game in python using  OOP

This is a simple Tetris game written in Python using object-oriented programming (OOP).

#libraries used

pygame: This library is used for creating multimedia applications, such as games.
random: This library is used for generating random numbers.
time: This library is used for managing time.
art: This library is used for generating ASCII art.
colorama: This library is used for coloring text in the console.

The pygame library is used to create the graphical user interface for the game. The random library is used to generate random Tetris shapes and colors. The time library is used to control the speed of the game. The art library is used to generate the ASCII art that is displayed at the beginning of the game. The colorama library is used to color the text in the console, which makes the game more visually appealing.

#classes used

The game is implemented using the following classes:

Figure: This class represents a falling block. It has the following attributes:
x: The X-coordinate of the block.
y: The Y-coordinate of the block.
type: The type of block. This is an integer that corresponds to one of the seven Tetris shapes.
color: The color of the block.
rotation: The rotation of the block.

Tetris: This class represents the Tetris game state. It has the following attributes:
level: The current level of the game.
score: The player's score.
state: The current state of the game. This can be start or gameover.
field: A two-dimensional array that represents the game grid.
height: The height of the game grid.
width: The width of the game grid.
x: The X-coordinate of the game grid.
y: The Y-coordinate of the game grid.
zoom: The zoom factor of the game grid.
figure: The current falling block.

The Figure class is used to represent the falling blocks. It has methods for moving the block, rotating the block, and getting the image of the block. The Tetris class is used to represent the Tetris game state. It has methods for updating the game state, drawing the game grid, and checking for game over.
The game ends when the board is full of Tetris pieces.

##How to build and run the game

To build and run the game, you will need to have a python interpreter with installed libraries for which one can use any python package manager, text editor or IDE(Integrated development environment) and access to command line
 
# Controls

- Left Arrow: Move the falling tetromino left.
- Right Arrow: Move the falling tetromino right.
- Down Arrow: Accelerate the falling speed of the tetromino.
- Up Arrow or Spacebar: Rotate the falling tetromino clockwise.
- Q Key: Quit the game.

# Features

- Smooth and responsive graphics using Pygame for an enjoyable gaming experience.
- Random generation of tetrominoes, ensuring each game is unique and challenging.
- Score tracking system, displaying the player's current score.
- Speed increment as the game progresses, making it more difficult over time.

##few tips

Try to keep the board as empty as possible. This will give you more room to manner new Tetris pieces. If you see a complete line, try to clear it as soon as possible. This will give you more points and make it easier to keep the board empty. Don't panic if the board starts to fill up. You can always try to rotate or move the current Tetris piece to a different location. Have fun!

![alt img](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.8PGGbt6oOTCHDM5BYT2SMAHaHa%26pid%3DApi&f=1&ipt=bfca43dc6cb847dbd9f084338b4a32c1860ba7e34a2af3e58894ee1b5c46065e&ipo=images)

![alt img](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.ZqKDCI6SjIq7tXRkd53QeAHaF0%26pid%3DApi&f=1&ipt=d1de0e2bebf518395293386994d3dab2dcd27c009d4ab5b6f0b2a40a2e257b65&ipo=images)
