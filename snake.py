import random


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

print_field()

# Snake
snake = [
    (FIELD_WIDTH // 2 + 3, FIELD_HEIGHT // 2),
    (FIELD_WIDTH // 2 + 2, FIELD_HEIGHT // 2),
    (FIELD_WIDTH // 2 + 1, FIELD_HEIGHT // 2),
]

DIRECTIONS = {"left": (-1, 0), "right": (1, 0), "up": (0, 1), "down": (0, -1)}
direction = input()
if direction == "w":
    move_to = DIRECTIONS["up"]
elif direction == "s":
    move_to = DIRECTIONS["down"]
elif direction == "a":
    move_to = DIRECTIONS["left"]
elif direction == "d":
    move_to = DIRECTIONS["right"]

# Apple
apple_pos = (random.randrange(0, 31), random.randrange(0, 15))
