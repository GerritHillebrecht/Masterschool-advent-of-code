from os.path import join
from config import dirname_input_files


def count_mas_tree(grid):
    num_rows = len(grid)
    num_cols = len(grid[0])

    x_mas_patterns = [
        [(-1, -1), (1, 1)],  # from top left to bottom right
        [(-1, 1), (1, -1)],  # from top right to bottom left
    ]

    # Have all "hit" coordinates
    return len([
        (row, col)
        # Leave the outer lines, since there can't be hits
        for row in range(1, num_rows - 1)
        for col in range(1, num_cols - 1)
        # Check both patterns for S and M
        if grid[row][col] == "A" and all(
            (grid[row + delta_row][col + delta_col] == 'M' and grid[row - delta_row][col - delta_col] == 'S') or
            (grid[row + delta_row][col + delta_col] == 'S' and grid[row - delta_row][col - delta_col] == 'M')
            for pattern in x_mas_patterns
            for delta_row, delta_col in pattern
        )
    ])


def count_word_appearences(grid, word):
    num_rows = len(grid)
    num_cols = len(grid[0])
    word_length = len(word)
    count = 0

    pattern = [
        (0, 1),  # horizontal right
        (0, -1),  # horizontal left
        (1, 0),  # vertical down
        (-1, 0),  # vertical up
        (1, 1),  # diagonal down-right
        (-1, -1),  # diagonal up-left
        (1, -1),  # diagonal down-left
        (-1, 1)  # diagonal up-right
    ]

    for row in range(num_rows):
        for col in range(num_cols):
            for delta_row, delta_col in pattern:
                if all(
                        # check grid edges
                        0 <= row + i * delta_row < num_rows and
                        0 <= col + i * delta_col < num_cols and

                        # check if characters match by increasing "radius" around char by 1 for each letter in word
                        grid[row + i * delta_row][col + i * delta_col] == word[i]
                        for i in range(word_length)
                ):
                    count += 1

    return count


def start_day_challenge():
    with open(join(dirname_input_files, "day_4_input_xmas_word_search.txt")) as handle:
        grid = list(map(lambda line: line.strip(), handle.readlines()))

    # Star 7: Count XMAS
    print("7. Number of xmas: ", count_word_appearences(grid, "XMAS"))

    # Star 8: Count MAS-trees
    print("8. Number of MAS-trees: ", count_mas_tree(grid))


if __name__ == "__main__":
    word_search = ["MMMSXXMASM", "MSAMXMSMSA", "AMXSXMAAMM", "MSAMASMSMX", "XMASAMXAMM", "XXAMMXXAMA", "SMSMSASXSS",
                   "SAXAMASAAA", "MAMMMXMMMM", "MXMXAXMASX"]

    word_to_find = "XMAS"
    print(count_word_appearences(word_search, word_to_find))

    start_day_challenge()
