from collections import deque

from config import dirname_input_files
from os.path import join


def get_garden_map():
    with open(join(dirname_input_files, "day_12_input_mock_garden_fences.txt"), "r") as handle:
        return [line.strip() for line in handle]


def get_plant_types(garden_map):
    return set(
        plant_type
        for row in garden_map
        for plant_type in row
    )


def get_regions(garden_map, plant_types):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    regions = deque()


def start_day_challenge():
    garden_map = get_garden_map()
    print(garden_map)
    plant_types = get_plant_types(garden_map)
    print(plant_types)
