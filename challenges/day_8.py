from os.path import join

from config import dirname_input_files

from math import ceil


def get_tower_map():
    with open(join(dirname_input_files, "day_8_input_tower_map.txt"), "r") as handle:
        return [line.strip() for line in handle]


def get_tower_positions(tower_map) -> list[tuple[int, int, str]]:
    return [
        (row_index, col_index, col)
        for row_index, row in enumerate(tower_map)
        for col_index, col in enumerate(row)
        if col != "."
    ]


def get_same_signal_towers(tower_positions, row, col, signal):
    return [
        same_tower
        for same_tower in tower_positions
        if same_tower[2] == signal and same_tower != (row, col, signal)
    ]


def get_antinodes(tower_map, tower_positions):
    rows, cols = len(tower_map), len(tower_map[0])
    antinodes = set()

    for row, col, signal in tower_positions:
        same_signal_towers = get_same_signal_towers(tower_positions, row, col, signal)

        for tower_row, tower_col, tower_signal in same_signal_towers:
            delta_y, delta_x = tower_row - row, tower_col - col

            if 0 <= (freq_row := tower_row + delta_y) < rows and 0 <= (freq_col := tower_col + delta_x) < cols:
                antinodes.add((freq_row, freq_col))

    return antinodes


def get_antinodes_harmony(tower_map, tower_positions):
    rows, cols = len(tower_map), len(tower_map[0])
    antinodes = set()

    for row, col, signal in tower_positions:
        same_signal_towers = get_same_signal_towers(tower_positions, row, col, signal)

        for tower_row, tower_col, tower_signal in same_signal_towers:
            delta_row, delta_col = tower_row - row, tower_col - col

            while 0 <= tower_row < rows and 0 <= tower_col < cols:
                antinodes.add((tower_row, tower_col))
                tower_row += delta_row
                tower_col += delta_col

    return antinodes


def start_day_challenge():
    tower_map = get_tower_map()
    tower_positions = get_tower_positions(tower_map)

    print(f"15. Unique frequency positions: {len(get_antinodes(tower_map, tower_positions))}")
    print(f"16. Unique frequency positions with harmony: {len(get_antinodes_harmony(tower_map, tower_positions))}")
