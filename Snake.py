from random import randrange as rnd
from operator import add
from sys import platform
from os import system as sys
from pytimedinput import timedInput
from colorama import Fore as color, init
from pyfiglet import figlet_format as ff


# Verifies the user OS in order to determine which command is going to be used to erase the screen
def verify_os():
    if platform == "win32" or platform == "cygwin":
        erasecmd = "cls"
    else:
        erasecmd = "clear"
    return erasecmd


# This function erases all the content on the screen, while the clear_screen reposition the cursor using an ANSI escape
# That creates the ilusion of cleaning the screen and fixes the flickering that used to happen when the game was running
def erase_screen():
    clearcmd = verify_os()
    sys(clearcmd)


# Moves the cursor back to the initial position, creating the ilusion that the screen is being cleaned.
# This function is used inside the game to create the ilusion of movement.
def clear_screen():
    sys("\033[H")


# A simple start menu, that asks the Player to press enter in order to start playing
def start_menu():
    erase_screen()
    text = "SNAKE.py"
    font = "banner3"
    menu_text = ff(text, font)
    print(color.LIGHTGREEN_EX + menu_text)
    input(color.LIGHTGREEN_EX + "> PRESS ANY BUTTON TO PLAY <")
    erase_screen()


# Define the basic controls for the Snake inside the game
def controls():
    global direction
    txt, time = timedInput("", timeout=0.1)
    match txt:
        case "w":
            direction = DIRECTIONS["up"]
        case "s":
            direction = DIRECTIONS["down"]
        case "a":
            direction = DIRECTIONS["left"]
        case "d":
            direction = DIRECTIONS["right"]
    return direction


# Creates the snake on the screen
def create_snake():
    x, y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
    return [(x, y), (x - 1, y), (x - 2, y)]


# Makes the snake move based on the direction provided by the player while calling the controls() function
def move_snake():
    global snake
    direction = controls()
    snake = [tuple(map(add, snake[0], direction))] + snake[:-1]


# Makes the snake grow when it eats the apple
def grow_snake():
    global snake, eaten
    if eaten:
        snake.append(snake[-1])
        eaten = False


# End the game if the Snake collides with a wall or it's own body
def kill_snake():
    if (
        snake[0][0] in (0, SCREEN_WIDTH - 1)
        or snake[0][1] in (0, SCREEN_HEIGHT - 1)
        or snake[0] in snake[1:]
    ):
        erase_screen()
        return True


# Creates the apple on the screen
def create_apple():
    x, y = rnd(1, SCREEN_WIDTH - 1), rnd(1, SCREEN_HEIGHT - 1)
    while (x, y) in snake:
        x, y = rnd(1, SCREEN_WIDTH - 1), rnd(1, SCREEN_HEIGHT - 1)
    return (x, y)


# Generate the Game Screen
def generate_screen():
    clear_screen()
    for cell in SCREEN:
        if cell == snake[0]:
            print(color.LIGHTGREEN_EX + "O", end="")
        elif cell in snake[1:]:
            print(color.LIGHTGREEN_EX + "o", end="")
        elif apple == cell:
            print(color.LIGHTRED_EX + "a", end="")
        elif cell[0] in (0, SCREEN_WIDTH - 1) or cell[1] in (0, SCREEN_HEIGHT - 1):
            print(color.LIGHTCYAN_EX + "#", end="")
        else:
            print(" ", end="")
        if cell[0] == SCREEN_WIDTH - 1:
            print("", end="\n")


# When the position of the snake's head is the same as the apple position, it triggers the "if" statement.
# Inside the "if", the code makes the apple disappear and spawn in another location by calling the create_apple function again.
# It also sets the eaten variable's value to true, which means that the Snake's body has to grow when the grow_snake function is called.
def eat_apple():
    global apple, eaten
    if apple == snake[0]:
        apple = create_apple()
        eaten = True


# Starts colorama
init(autoreset=True)

# CREATING THE SCREEN
# Defines the screen size
SCREEN_WIDTH = 32
SCREEN_HEIGHT = 16
# Creates the screen by defining all the cells in the Screen, based on the width and height that has been set previously
SCREEN = [(col, row) for row in range(SCREEN_HEIGHT) for col in range(SCREEN_WIDTH)]

# This dictionary contains the directions the Snake can move to, and the values that are going to be changed so it moves.
DIRECTIONS = {"left": (-1, 0), "right": (1, 0), "up": (0, -1), "down": (0, 1)}
direction = DIRECTIONS["right"]

# Creates the Snake and the apple on the Screen.
snake = create_snake()
apple = create_apple()
# The "eaten" variable is created here, with the default value set on "False".
eaten = False

# Shows the start menu to the player
start_menu()

# The game runs inside this loop, until the snake dies
while True:
    generate_screen()
    move_snake()
    eat_apple()
    grow_snake()
    if kill_snake():
        break
