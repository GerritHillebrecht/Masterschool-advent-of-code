import re
from os.path import join

from config import dirname_input_files

pattern_mul = r'mul\((\d+,\d+)\)'
pattern_do = r"(do(?:n't)?\(\))|(mul\((\d+,\d+)\))"
example = "do()xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
filename_input_corrupted_data = "day_3_input_corrupted_data.txt"


def read_file(filename):
    with open(join(dirname_input_files, filename)) as handle:
        return handle.read()


def get_number_pairs(data):
    return list(map(
        lambda pair: tuple(pair.split(",")),
        re.findall(pattern_mul, data)
    ))


def get_sum_of_corrupted_data(data):
    # Get all number pairs
    number_pairs = get_number_pairs(data)

    return sum(
        int(num1) * int(num2)
        for [num1, num2] in number_pairs
    )


def get_sum_of_corrupted_data_respecting_dos(data):
    matches = re.finditer(pattern_do, f"do(){data}")

    context = None
    pairs_with_context = []

    # if match is a do/don't: Set the context. Otherwise, append with context
    for match in matches:
        if match.group(1):
            context = match.group(1)
        elif match.group(2) and context:
            pairs_with_context.append((context, match.group(3)))

    pairs_with_context = [
        [int(x), int(y)]
        for context, pair in pairs_with_context
        if "don't()" not in context
        for x, y in [pair.split(",")]
    ]

    return sum(x * y for x, y in pairs_with_context)


def start_day_challenge():
    # Read the corrupted data
    corrupted_data = read_file(filename_input_corrupted_data)

    # Star 5: Fix corrupted data
    print("5. The sum of all corrupted multiplications: ", get_sum_of_corrupted_data(corrupted_data))

    # Star 6: Include do() instruction
    print("6. Respect do() instruction: ", get_sum_of_corrupted_data_respecting_dos(corrupted_data))
