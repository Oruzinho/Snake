import random
import operator
from pytimedinput import timedInput
import os


def update_snake():
    direction = DIRECTIONS["left"]
    txt, time = timedInput("", timeout=0.3)
    match txt:
        case "w":
            direction = DIRECTIONS["up"]
        case "s":
            direction = DIRECTIONS["down"]
        case "a":
            direction = DIRECTIONS["left"]
        case "d":
            direction = DIRECTIONS["right"]
    new_head = snake[0][0] + direction[0], snake[0][1] + direction[1]
    snake.insert(0, new_head)
    snake.pop(-1)


def print_field():
    for cell in CELLS:
        # print(cell)
        if cell in snake:
            print("X", end="")
        elif cell[0] in (0, FIELD_WIDTH - 1) or cell[1] in (0, FIELD_HEIGHT - 1):
            print("#", end="")
        elif cell == apple_pos:
            print("@", end="")
        else:
            print(".", end="")
        if cell[0] == FIELD_WIDTH - 1:
            print("", end="\n")


# Scenario
FIELD_WIDTH = 32
FIELD_HEIGHT = 16
CELLS = [(col, row) for row in range(FIELD_HEIGHT) for col in range(FIELD_WIDTH)]

# Snake
snake = [
    (FIELD_WIDTH // 2 + 3, FIELD_HEIGHT // 2),
    (FIELD_WIDTH // 2 + 2, FIELD_HEIGHT // 2),
    (FIELD_WIDTH // 2 + 1, FIELD_HEIGHT // 2),
]

DIRECTIONS = {"left": (-1, 0), "right": (1, 0), "up": (0, -1), "down": (0, 1)}

# Apple
apple_pos = (random.randrange(0, 31), random.randrange(0, 15))

while True:
    os.system("cls")
    print_field()
    update_snake()
