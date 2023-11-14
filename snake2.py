from random import randrange as rnd
from operator import add
from sys import platform
from os import system as sys
from pytimedinput import timedInput


def verify_os():
    if platform == "win32" or platform == "cygwin":
        clearcmd = "cls"
    else:
        clearcmd = "clear"
    return clearcmd


def controls():
    global direction
    txt, time = timedInput("", timeout=0.2)
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


def create_snake():
    x, y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
    return [(x + 3, y), (x + 2, y), (x + 1, y)]


def move_snake():
    global snake
    direction = controls()
    snake = [tuple(map(add, snake[0], direction))] + snake[:-1]


def grow_snake():
    global snake, eaten
    if eaten:
        snake.append(snake[-1])
        eaten = False


def kill_snake():
    if (
        snake[0][0] in (0, SCREEN_WIDTH - 1)
        or snake[0][1] in (0, SCREEN_HEIGHT - 1)
        or snake[0] in snake[1:]
    ):
        sys(clearcmd)
        return True


def create_apple():
    x, y = rnd(1, SCREEN_WIDTH - 1), rnd(1, SCREEN_HEIGHT - 1)
    while (x, y) in snake:
        x, y = rnd(1, SCREEN_WIDTH - 1), rnd(1, SCREEN_HEIGHT - 1)
    return (x, y)


def generate_screen():
    for cell in SCREEN:
        if cell == snake[0]:
            print("O", end="")
        elif cell in snake[1:]:
            print("o", end="")
        elif apple == cell:
            print("a", end="")
        elif cell[0] in (0, SCREEN_WIDTH - 1) or cell[1] in (0, SCREEN_HEIGHT - 1):
            print("#", end="")
        else:
            print(" ", end="")
        if cell[0] == SCREEN_WIDTH - 1:
            print("", end="\n")


def eat_apple():
    global apple, eaten
    if apple == snake[0]:
        apple = create_apple()
        eaten = True


SCREEN_WIDTH = 32
SCREEN_HEIGHT = 16
SCREEN = [(col, row) for row in range(SCREEN_HEIGHT) for col in range(SCREEN_WIDTH)]
DIRECTIONS = {"left": (-1, 0), "right": (1, 0), "up": (0, -1), "down": (0, 1)}
direction = DIRECTIONS["right"]

snake = create_snake()
apple = create_apple()
eaten = False

clearcmd = verify_os()

while True:
    sys(clearcmd)
    generate_screen()
    move_snake()
    eat_apple()
    grow_snake()
    if kill_snake() == True:
        break
