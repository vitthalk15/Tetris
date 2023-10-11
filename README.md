# Tetris game using pygame
OOPS project

This is a simple Tetris game written in Python using object-oriented programming (OOP). 

It is created using Pygame. It is a classic implementation of the famous Tetris game built in Python using the Pygame library for graphics and game development. It provides a fun and addictive gaming experience where players aim to clear lines by strategically arranging falling blocks called "tetrominoes."



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

How to build and run the game

To build and run the game, you will need to have a python compiler installed. Once you have a compiler installed, you can build the game by running the following command:

./tetris 

Tips for playing the game

Here are a few tips for playing the game:

Try to keep the board as empty as possible. This will give you more room to maneuver new Tetris pieces. If you see a complete line, try to clear it as soon as possible. This will give you more points and make it easier to keep the board empty. Don't panic if the board starts to fill up. You can always try to rotate or move the current Tetris piece to a different location. Have fun!
