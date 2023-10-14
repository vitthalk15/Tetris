import pygame
import random
import time
import threading

from art import text2art
from art import *
from colorama import Fore, Style, init

import Tetris_Figures
from Tetris_Class import Tetris


#Prrinting Tetris at the start
init(autoreset=True)
ascii_art = text2art("Tetris", font='block', chr_ignore=True)                     
colors = [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW, Fore.MAGENTA, Fore.CYAN]  #defining colours
ascii_characters = list(ascii_art)    
colored_art = ""
for i, char in enumerate(ascii_characters):
    if char == '\n':
        colored_art += char  
    else:
        colored_art += colors[i % len(colors)] + char
print(colored_art)
print(Style.RESET_ALL)


#Displaying the time remaining for the game to start
def countdown():
    delay_seconds = 10      # Number of seconds before starting
    for remaining_time in range(delay_seconds, 0, -1):
        if countdown_flag.is_set():
            break
        print(f"Game starts in {remaining_time} seconds", end='\r')
        time.sleep(1)
    print(" " * 40, end='\r')  # Clear the countdown display

# Create a thread for the countdown
countdown_thread = threading.Thread(target=countdown)
countdown_flag = threading.Event()

#Displaying game rules
print(Fore.GREEN + "Game Rules: \n")
print(Fore.CYAN + "1. Press " + Fore.RED + " → " + Fore.CYAN + "and" + Fore.RED + " ← " + Fore.CYAN + "keys to move right and left respectively \n")
print(Fore.CYAN + "2. Press " + Fore.RED + "↑" + Fore.CYAN + " to rotate \n")
print(Fore.CYAN + "3. Press " + Fore.RED + "↓" + Fore.CYAN + " to move faster \n")
print(Fore.CYAN + "4. Press " + Fore.RED + "space bar" + Fore.CYAN + " to rest tetromino on the game board \n")

countdown_thread.start()
# Wait for the user to press Enter to start the game
input(Fore.MAGENTA+"Press Enter to start the game\n")

# Set the flag to stop the countdown
countdown_flag.set()
countdown_thread.join()

print("Game starts now!")


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

# Initialize the game engine
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

size = (400, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Tetris")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
fps = 375
game = Tetris(20, 10)
counter = 0

pressing_down = False

while not done:
    if game.figure is None:
        game.new_figure()
    counter += 1
    if counter > 100000:
        counter = 0

    if counter % (fps // game.level // 2) == 0 or pressing_down:
        if game.state == "start":
            game.go_down()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                game.rotate()
            if event.key == pygame.K_DOWN:
                pressing_down = True
            if event.key == pygame.K_LEFT:
                game.go_side(-1)
            if event.key == pygame.K_RIGHT:
                game.go_side(1)
            if event.key == pygame.K_SPACE:
                game.go_space()
            if event.key == pygame.K_ESCAPE:
                game.__init__(20, 10)

    if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                pressing_down = False

    screen.fill(WHITE)

    for i in range(game.height):
        for j in range(game.width):
            pygame.draw.rect(screen, GRAY, [game.x + game.zoom * j, game.y + game.zoom * i, game.zoom, game.zoom], 1)
            if game.field[i][j] > 0:
                pygame.draw.rect(screen, colors[game.field[i][j]],
                                 [game.x + game.zoom * j + 1, game.y + game.zoom * i + 1, game.zoom - 2, game.zoom - 1])

    if game.figure is not None:
        for i in range(4):
            for j in range(4):
                p = i * 4 + j
                if p in game.figure.image():
                    pygame.draw.rect(screen, colors[game.figure.color],
                                     [game.x + game.zoom * (j + game.figure.x) + 1,
                                      game.y + game.zoom * (i + game.figure.y) + 1,
                                      game.zoom - 2, game.zoom - 2])

    font = pygame.font.SysFont('Calibri', 25, True, False)
    font1 = pygame.font.SysFont('Calibri', 65, True, False)
    text = font.render("Score: " + str(game.score), True, BLACK)
    text_game_over = font1.render("Game Over", True, (255, 125, 0))
    text_game_over1 = font1.render("Press ESC", True, (255, 215, 0))

    screen.blit(text, [0, 0])
    if game.state == "gameover":
        screen.blit(text_game_over, [20, 200])
        screen.blit(text_game_over1, [25, 265])

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
tprint("Thank You","caligraphy")
