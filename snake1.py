from random import randint as randi
import operator
from pytimedinput import timedInput
import os


def update_snake():
    global direction, eaten
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
    new_head = snake_body[0][0] + direction[0], snake_body[0][1] + direction[1]
    snake_body.insert(0, new_head)
    if not eaten:
        snake_body.pop(-1)
    eaten = False


def print_field():
    for cell in CELLS:
        # print(cell)
        if cell in snake_body:
            print("X", end="")
        elif cell[0] in (0, FIELD_WIDTH - 1) or cell[1] in (0, FIELD_HEIGHT - 1):
            print("#", end="")
        elif cell == apple_pos:
            print("@", end="")
        else:
            print(".", end="")
        if cell[0] == FIELD_WIDTH - 1:
            print("", end="\n")


def place_apple():
    col = randi(1, FIELD_WIDTH - 2)
    row = randi(1, FIELD_HEIGHT - 2)
    while (col, row) in snake_body:
        col = randi(1, FIELD_WIDTH - 2)
        row = randi(1, FIELD_HEIGHT - 2)
    return (col, row)


def apple_collision():
    global apple_pos, eaten
    if apple_pos == snake_body[0]:
        apple_pos = place_apple()
        eaten = True


# Scenario
FIELD_WIDTH = 32
FIELD_HEIGHT = 16
CELLS = [(col, row) for row in range(FIELD_HEIGHT) for col in range(FIELD_WIDTH)]

# Snake
snake_body = [
    (FIELD_WIDTH // 2 + 3, FIELD_HEIGHT // 2),
    (FIELD_WIDTH // 2 + 2, FIELD_HEIGHT // 2),
    (FIELD_WIDTH // 2 + 1, FIELD_HEIGHT // 2),
]

DIRECTIONS = {"left": (-1, 0), "right": (1, 0), "up": (0, -1), "down": (0, 1)}
direction = DIRECTIONS["right"]

# Apple
apple_pos = place_apple()
eaten = False

while True:
    os.system("cls")
    print_field()
    update_snake()
    apple_collision()
    if (
        snake_body[0][0] in (0, FIELD_WIDTH - 1)
        or snake_body[0][1] in (0, FIELD_HEIGHT - 1)
        or snake_body[0] in snake_body[1:]
    ):
        os.system("cls")
        break
