import sys
from os.path import join

from config import dirname_input_files

sys.setrecursionlimit(10000)

SYMBOLS = [".", "#", "X"]
LOOP_SYMBOL = "0"

move_directions = {"north": (-1, 0), "east": (0, 1), "south": (1, 0), "west": (0, -1)}

direction_symbols = {
    "north": "^",
    "east": ">",
    "south": "v",
    "west": "<"
}

directions = [*move_directions]


def get_map():
    with open(join(dirname_input_files, "day_6_input_map.txt")) as handle:
        return [
            list(line.strip())
            for line in handle.readlines()
        ]


def get_next_direction(current_direction):
    current_index = directions.index(current_direction)
    next_index = (current_index + 1) % len(directions)
    return directions[next_index]


def check_for_loops(lab_map):
    print("Started checking for loops - may take a while.")
    # Get starting position of input map
    start_row, start_col = calculate_current_position(lab_map)

    loop_hits = []

    # Get number of rows and cols
    rows, cols = len(lab_map), len(lab_map[0])

    def does_loop_exist(new_row, new_col):
        # Define initials positions
        current_row, current_col = start_row, start_col
        # Default direction as given in the task
        direction = "north"
        # use set to eliminate duplicate entries
        visited = set()

        while True:
            # Check if current position is already visited with the same direction
            if (current_row, current_col, direction) in visited:
                return True

            # Add current position with direction
            visited.add((current_row, current_col, direction))

            # Get delta values for movement
            y, x = move_directions[direction]
            next_row, next_col = current_row + y, current_col + x

            # Return False if Index is out of bounds (left the field)
            if not (0 <= next_row < rows and 0 <= next_col < cols):
                return False

            # If the next calculated position matches the position where a new obstacle was added,
            # change the direction to the next one clockwise, then recalculate the next position
            # based on the new direction.
            if next_row == new_row and next_col == new_col:
                direction = get_next_direction(direction)
                y, x = move_directions[direction]
                next_row, next_col = current_row + y, current_col + x

            # Switch up 90° if hitting a "#"
            if lab_map[next_row][next_col] == "#":
                direction = get_next_direction(direction)
                continue

            # update current_row and current_col and continue the loop
            current_row, current_col = next_row, next_col

    # Loop every element in the field if it is a "."
    for row in range(rows):
        for col in range(cols):
            if lab_map[row][col] == ".":
                if does_loop_exist(row, col):
                    loop_hits.append((row, col))

    return loop_hits


def calculate_route(lab_map):
    current_position = calculate_current_position(lab_map)

    def calculate_steps(lab_map):
        return sum(
            1
            for row in lab_map
            for col in row
            if col == "X"
        )

    def move_forward(current_row, current_col, direction="north"):
        y, x = move_directions[direction]
        next_row = current_row + y
        next_col = current_col + x

        lab_map[current_row][current_col] = "X"

        if not all([
            0 <= next_row <= len(lab_map) - 1,
            0 <= next_col <= len(lab_map[0])
        ]):
            return

        next_step = lab_map[next_row][next_col]

        if next_step in [".", "X"]:
            return move_forward(current_row=next_row, current_col=next_col, direction=direction)

        if next_step == "#":
            next_direction = get_next_direction(direction)
            y, x = move_directions[next_direction]
            next_row = current_row + y
            next_col = current_col + x
            return move_forward(current_row=next_row, current_col=next_col, direction=next_direction)

    move_forward(current_position[0], current_position[1])
    return calculate_steps(lab_map)


def calculate_current_position(lab_map):
    for index_row, row in enumerate(lab_map):
        for index_col, col in enumerate(row):
            if col not in SYMBOLS:
                return index_row, index_col


def start_day_challenge(massive_loop=False):
    lab_map = get_map()

    # 11. Get unique positions
    print(f"11. Unvisited positions: {calculate_route(lab_map)}")

    # 12. Loops
    if massive_loop:
        lab_map = get_map()
        print(f"12. Number of obstacles that invoke a loop: {len(check_for_loops(lab_map))}")
