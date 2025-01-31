from os.path import join
from config import dirname_input_files


def get_topographic_map():
    with open(join(dirname_input_files, "day_10_input_topograhical_map.txt"), "r") as handle:
        return [list(map(int, line.strip())) for line in handle]


def get_trailhead_positions(topographic_map):
    return [
        (row_index, col_index)
        for row_index, row in enumerate(topographic_map)
        for col_index, topographical_point in enumerate(row)
        if str(topographical_point) == "0"
    ]


def get_trailhead_scores(trailheads, topographic_map, type="score"):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    rows = len(topographic_map)
    cols = len(topographic_map[0])

    def trailhead_score(trailhead_row, trailhead_col):
        all_paths = set()

        def find_path(row, col, trailhead_path):
            elevation = topographic_map[row][col]

            if topographic_map[row][col] == 9:
                full_path = ", ".join([f"{topographic_map[y][x]}: ({y},{x})" for y, x in trailhead_path + [(row, col)]])
                all_paths.add(full_path if type == "rating" else (row, col))
                return

            for delta_row, delta_col in directions:
                next_row, next_col = row + delta_row, col + delta_col
                if 0 <= next_row < rows and 0 <= next_col < cols:
                    if topographic_map[next_row][next_col] == elevation + 1:
                        find_path(next_row, next_col, trailhead_path + [(row, col)])

        find_path(trailhead_row, trailhead_col, [])

        return all_paths

    return sum(
        len(trailhead_score(trailhead_row, trailhead_col))
        for trailhead_row, trailhead_col in trailheads
    )


def start_day_challenge():
    topographic_map = get_topographic_map()
    trailhead_positions = get_trailhead_positions(topographic_map)
    trailhead_scores = get_trailhead_scores(trailhead_positions, topographic_map)
    trailhead_scores_rating = get_trailhead_scores(trailhead_positions, topographic_map, "rating")

    print("19. Trailhead scores:", trailhead_scores)
    print("20. Trailhead ratings:", trailhead_scores_rating)
