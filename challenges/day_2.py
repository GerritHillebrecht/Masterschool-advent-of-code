from os.path import join

from config import dirname_input_files
from utils.storage import save_to_file, read_from_file

filename_records = "day_2_input_reactor_levels.txt"
filename_json_storage = "day_2_reactor_levels.json"

MAX_DIFFERENCE = 3


def create_json_file():
    with open(join(dirname_input_files, filename_records)) as handle:
        data = [
            [int(level) for level in row.strip().split(" ")]
            for row in handle.readlines()
        ]

        save_to_file(data, filename_json_storage)


def get_number_of_safe_reports():
    reports = read_from_file(filename_json_storage)

    return len([
        report
        for report in reports
        if is_safe_report(report)
    ])


def get_number_of_safe_reports_with_dampener():
    reports = read_from_file(filename_json_storage)

    return len([
        report
        for report in reports
        if is_safe_report_with_dampener(report)
    ])


def is_safe_report(report):
    return all([
        is_monotonic(report),
        is_within_difference_limit(report)
    ])


def is_safe_report_with_dampener(report):
    if is_safe_report(report):
        return True

    for index in range(len(report)):
        shortened_report = [*report]
        del shortened_report[index]

        if is_safe_report(shortened_report):
            return True

    return False


def is_monotonic(report):
    increasing = all(report[i] < report[i + 1] for i in range(len(report) - 1))
    decreasing = all(report[i] > report[i + 1] for i in range(len(report) - 1))

    return increasing or decreasing


def is_within_difference_limit(report, limit=MAX_DIFFERENCE):
    return all(abs(report[i] - report[i + 1]) <= limit for i in range(len(report) - 1))


def start_day_2():
    # Create JSON File
    create_json_file()

    # Star 3: Get number of safe reports
    number_of_safe_reports = get_number_of_safe_reports()
    print("3. Safe reports: ", number_of_safe_reports)

    # Star 4: Get number of safe reports with error margin
    number_of_safe_reports = get_number_of_safe_reports_with_dampener()
    print("4. Safe reports after dampening: ", number_of_safe_reports)
