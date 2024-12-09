from collections import Counter
from os.path import join

from config import dirname_input_files


def get_disk_map():
    with open(join(dirname_input_files, "day_9_input_disk_map.txt")) as handle:
        return handle.read()


def create_individual_blocks(disk_map) -> list[int]:
    int_disk_map = list(map(int, disk_map))

    return [
        int(index / 2) if index % 2 == 0 else "."
        for index, amount in enumerate(int_disk_map)
        for _ in range(int(amount))
    ]


def create_files(disk_map) -> list[list[int]]:
    int_disk_map = list(map(int, disk_map))

    return [
        [
            int(index / 2) if index % 2 == 0 else "."
            for _ in range(int(amount))
        ]
        for index, amount in enumerate(int_disk_map)
    ]


def move_whole_files(lst: list):
    numbers_list = [num for num in lst if "." not in num]
    numbers_list.reverse()

    for index, number_list in enumerate(numbers_list):
        num_list_index = lst.index(numbers_list[index])
        num_list_length = len(number_list)

        available_slots = [
            (index, len(item))
            for index, item in enumerate(lst)
            if "." in item and len(item) >= num_list_length and index < num_list_index
        ]

        if len(available_slots) > 0:
            # print(available_slots)
            index_slot, slot_length = available_slots[0]
            lst.pop(num_list_index)
            lst.insert(num_list_index, ["." for _ in range(num_list_length)])
            lst[index_slot] = lst[index_slot][num_list_length:]
            lst.insert(index_slot, number_list)

    return lst


def move_file_blocks(block_list: list[int]) -> list[int]:
    dot_index, number_index = 0, len(block_list) - 1

    # Loop until front and back reached same index/position
    while dot_index < number_index:
        # get next dot index
        while dot_index < len(block_list) and block_list[dot_index] != '.':
            dot_index += 1
        # get next number index
        while number_index >= 0 and block_list[number_index] == '.':
            number_index -= 1
        # swap number with dot
        if dot_index < number_index:
            block_list[dot_index], block_list[number_index] = block_list[number_index], block_list[dot_index]
            dot_index += 1
            number_index -= 1

    return block_list


def filesystem_checksum(file_blocks):
    return sum(
        index * number
        for index, number in enumerate(list(file_blocks))
        if number != "."
    )


def start_day_challenge(massive_loop=False):
    disk_map = get_disk_map()
    individual_blocks = create_individual_blocks(disk_map)
    moved_file_blocks = move_file_blocks(individual_blocks)
    checksum = filesystem_checksum(moved_file_blocks)

    # 17. Checksum of rearranged blocks
    print("17. Checksum of rearranged blocks:", checksum)

    individual_files = create_files(disk_map)
    moved_whole_files = move_whole_files(individual_files)
    checksum_files = filesystem_checksum([col for row in moved_whole_files for col in row])
    # 18. Checksum of rearranged files
    if massive_loop:
        print("18. Checksum of rearranged files", checksum_files)
