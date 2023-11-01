import random


def move_snake():
    direction = input()
    if direction == "w":
        move_to = DIRECTIONS["up"]
    elif direction == "s":
        move_to = DIRECTIONS["down"]
    elif direction == "a":
        move_to = DIRECTIONS["left"]
    elif direction == "d":
        move_to = DIRECTIONS["right"]
    return move_to


def define_snake_position():
    snake_x = SCREEN_WIDTH // 2
    snake_y = SCREEN_HEIGHT // 2
    return [(snake_x + 3, snake_y), (snake_x + 2, snake_y), (snake_x + 1, snake_y)]


def define_apple_position():
    apple_x = random.randrange(1, SCREEN_WIDTH - 1)
    apple_y = random.randrange(1, SCREEN_HEIGHT - 1)
    return (apple_x, apple_y)


def generate_screen():
    for cell in SCREEN:
        if cell in snake_position:
            print("X", end="")
        elif apple_position == cell:
            print("@", end="")
        elif cell[0] in (0, SCREEN_WIDTH - 1) or cell[1] in (0, SCREEN_HEIGHT - 1):
            print("#", end="")
        else:
            print(".", end="")
        if cell[0] == SCREEN_WIDTH - 1:
            print("", end="\n")


SCREEN_WIDTH = 32
SCREEN_HEIGHT = 16
SCREEN = [(col, row) for row in range(SCREEN_HEIGHT) for col in range(SCREEN_WIDTH)]
DIRECTIONS = {"left": (-1, 0), "right": (1, 0), "up": (0, 1), "down": (0, -1)}

snake_position = define_snake_position()

apple_position = define_apple_position()

generate_screen()
