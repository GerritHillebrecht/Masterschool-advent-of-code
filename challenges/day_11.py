from functools import lru_cache, cache
from os.path import join

from config import dirname_input_files


def get_stones():
    with open(join(dirname_input_files, "day_11_input_alien_stones.txt")) as handle:
        return list(map(int, handle.read().split(" ")))


@lru_cache(maxsize=None)
def split_or_multiply(stone):
    """Funktion, die einen Stein verarbeitet, entweder aufteilt oder multipliziert."""
    if stone == 0:
        return (1,)
    stone_str = str(stone)
    stone_len = len(stone_str)
    if stone_len % 2 == 0:
        mid = stone_len // 2
        return int(stone_str[:mid]), int(stone_str[mid:])
    else:
        return (stone * 2024,)


@cache
def stone_count(stone, steps):
    if steps == 0:
        return 1
    if stone == 0:
        return stone_count(1, steps - 1)

    stone_str = str(stone)
    stone_len = len(stone_str)

    if stone_len % 2 == 0:
        mid = stone_len // 2
        left_half_stone = int(stone_str[:mid])
        right_half_stone = int(stone_str[mid:])

        return stone_count(left_half_stone, steps - 1) + stone_count(right_half_stone, steps - 1)
    return stone_count(stone * 2024, steps - 1)


def start_day_challenge():
    stones = get_stones()
    print(f"21. Stones after 25 blinks:", sum(stone_count(stone, 25) for stone in stones))
    print(f"22. Stones after 75 blinks:", sum(stone_count(stone, 75) for stone in stones))
