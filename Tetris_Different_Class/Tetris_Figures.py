import pygame
import random
import time

from art import text2art
from art import *
from colorama import Fore, Style, init

#Defining colours for the program
colors = [
        (0, 0, 0),
        (120, 37, 179),
        (100, 179, 179),
        (80, 34, 22),
        (80, 134, 22),
        (180, 34, 22),
        (180, 34, 122),
        ]

# Class for the shapes of tetrominoes
class Figure:
    x = 0
    y = 0

    figures = [
        [[1, 5, 9, 13], [4, 5, 6, 7]],     #I Tetromino
        [[4, 5, 9, 10], [2, 6, 5, 9]],     #Z Tetromino
        [[6, 7, 9, 10], [1, 5, 6, 10]],    #S Tetromino
        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],   #J Tetromino
        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]], #L Tetromino
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],    #T Tetromino
        [[1, 2, 5, 6]],   #O Tetromino
    ]

# defining coordinates and movement of tetromino
    def __init__(self, x, y):
        
        
        self.x = x
        self.y = y
        self.type = random.randint(0, len(self.figures) - 1)
        self.color = random.randint(1, len(colors) - 1)
        self.rotation = 0

    def image(self):
        return self.figures[self.type][self.rotation]

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.figures[self.type])
