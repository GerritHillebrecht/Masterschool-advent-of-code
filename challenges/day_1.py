from collections import Counter
from os.path import join

from config import dirname_input_files
from utils import save_to_file, read_from_file

filename_input = "day_1_input_location_ids.txt"
filename_team_one = "list_team_1.json"
filename_team_two = "list_team_2.json"


def create_separate_lists(input_file):
    list_team_one = []
    list_team_two = []

    with open(join(dirname_input_files, input_file), "r") as handle:
        for row in handle.readlines():
            [num1, num2] = row.strip().split("   ")

            try:
                list_team_one.append(int(num1))
                list_team_two.append(int(num2))
            except ValueError:
                print("You failed to copy the input from advent of code. Great job!")

    save_to_file(sorted(list_team_one), filename_team_one)
    save_to_file(sorted(list_team_two), filename_team_two)


def get_differences_between_lists(list_team_one, list_team_two):
    # Check if the prepared lists are indeed of the same length
    same_length = len(list_team_one) == len(list_team_two)

    if not same_length:
        return "You fucked up along the way"

    # Return the sum of the absolute distances between the ids
    return sum(
        abs(list_team_one[idx] - list_team_two[idx])
        for idx in range(len(list_team_one))
    )


def get_similarities_between_lists(list_team_one, list_team_two):
    # create counter for linear (O(n)/O(2n)) instead of squared O(n^2) time-complexity.
    counter = Counter(list_team_two)

    # sum up results
    return sum(
        list_team_one[idx] * counter[list_team_one[idx]]
        for idx in range(len(list_team_two))
    )


def start_day_1():
    # Preparation, create separate lists
    create_separate_lists(filename_input)

    list_one = read_from_file(filename_team_one)
    list_two = read_from_file(filename_team_two)

    # Star 1:
    differences = get_differences_between_lists(list_one, list_two)
    print("1. Differences:", differences)

    # Star 2:
    similarities = get_similarities_between_lists(list_one, list_two)
    print("2. Similarities:", similarities)
