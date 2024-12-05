from math import floor
from os.path import join
from config import dirname_input_files


def get_updates():
    with open(join(dirname_input_files, "day_5_input_updates.txt"), "r") as handle:
        return [
            [*map(int, row.strip().split(","))]
            for row in handle.readlines()
        ]


def get_requirements():
    requirements = {}
    with open(join(dirname_input_files, "day_5_input_requirements.txt")) as handle:
        for line in handle.readlines():
            first, second = map(int, line.strip().split("|"))

            if first not in requirements:
                requirements[first] = set()

            requirements[first].add(second)
        return requirements


def get_incorrect_updates(updates, requirements):
    correct_update_indices = get_indices_of_correct_updates(updates=updates, requirements=requirements)

    return [
        update
        for idx, update in enumerate(updates)
        if idx not in correct_update_indices
    ]


def get_indices_of_correct_updates(updates, requirements):
    return [
        index
        for index, update in enumerate(updates)
        if all(
            # Filter if the page_number or all pages that have to come after are not in the update.
            (page_numer not in update or all(
                criteria_page_number not in update
                for criteria_page_number in criteria
            )) or
            # Otherwise check if the index of the page is smaller than of all the criteria pages
            update.index(page_numer) < min(
                update.index(criteria_page_number)
                for criteria_page_number in criteria
                if criteria_page_number in update
            )
            for page_numer, criteria in requirements.items()
        )
    ]


def get_sum_middle_pages(requirements, updates):
    correct_update_indices = get_indices_of_correct_updates(updates=updates, requirements=requirements)

    return sum(
        # Return the middle page
        updates[update_index][floor(len(updates[update_index]) / 2)]
        # loop all updates
        for update_index in correct_update_indices
    )


def get_sum_of_incorrect_updates(updates, requirements):
    incorrect_updates = get_incorrect_updates(updates, requirements)

    return sum(
        update[floor(len(update) / 2)]
        for update in map(lambda update: sort_update(update, requirements), incorrect_updates)
    )


def sort_update(update: list[int], requirements: dict[int, set[int]]):
    sorted_update = [*update]

    for index, page in enumerate(sorted_update):
        if index == 0:
            continue

        if page in requirements:
            page_restrictions = set(filter(
                lambda requirement: requirement in sorted_update,
                requirements.get(page)
            ))

            for idx in range(index):
                previous_page = sorted_update[idx]
                if previous_page in page_restrictions:
                    sorted_update.pop(index)
                    sorted_update.insert(idx, page)
                    break

    return sorted_update


def start_day_challenge():
    updates: list[list[int]] = get_updates()
    requirements: dict[int, set[int]] = get_requirements()

    # 9. Star: Sum of middle number of correct updates
    print(f"9. Sum of middle page numbers of correct updates:  {get_sum_middle_pages(requirements, updates)}")

    # 10. Star: Sum of middle number of incorrect Updates
    print(f"10. Sum of middle page numbers of incorrect updates after sorting: {get_sum_of_incorrect_updates(updates, requirements)}")
