import random
import operator
from pytimedinput import timedInput


def controls():
    control = input()
    if control == "w":
        direction = DIRECTIONS["up"]
    elif control == "s":
        direction = DIRECTIONS["down"]
    elif control == "a":
        direction = DIRECTIONS["left"]
    elif control == "d":
        direction = DIRECTIONS["right"]
    return direction


def create_snake():
    snake_x = SCREEN_WIDTH // 2
    snake_y = SCREEN_HEIGHT // 2
    return [(snake_x + 3, snake_y), (snake_x + 2, snake_y), (snake_x + 1, snake_y)]


def create_apple():
    apple_x = random.randrange(1, SCREEN_WIDTH - 1)
    apple_y = random.randrange(1, SCREEN_HEIGHT - 1)
    return (apple_x, apple_y)


def generate_screen():
    for cell in SCREEN:
        if cell in snake:
            print("X", end="")
        elif apple == cell:
            print("@", end="")
        elif cell[0] in (0, SCREEN_WIDTH - 1) or cell[1] in (0, SCREEN_HEIGHT - 1):
            print("#", end="")
        else:
            print(".", end="")
        if cell[0] == SCREEN_WIDTH - 1:
            print("", end="\n")


def move_snake():
    direction = controls()
    snake[2] = snake[1]
    snake[1] = snake[0]
    snake[0] = tuple(map(operator.add, snake[0], direction))


SCREEN_WIDTH = 32
SCREEN_HEIGHT = 16
SCREEN = [(col, row) for row in range(SCREEN_HEIGHT) for col in range(SCREEN_WIDTH)]
DIRECTIONS = {"left": (-1, 0), "right": (1, 0), "up": (0, -1), "down": (0, 1)}

snake = create_snake()
apple = create_apple()

while True:
    generate_screen()
    txt, time = timedInput("", timeout=0.3)
    move_snake()
