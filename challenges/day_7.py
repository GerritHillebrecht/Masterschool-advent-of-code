from os.path import join
from config import dirname_input_files
from functools import cache
from operator import add, mul

OPERATORS = [add, mul]


def get_equations():
    with open(join(dirname_input_files, "day_7_input_operators.txt"), "r") as handle:
        equations = []
        for line in handle:
            result, *operands = line.strip().split(" ")
            equations.append([int(result[:-1]), list(map(int, operands))])
        return equations


def get_sum_equations(equations):
    return sum(
        result
        for result, operands in equations
        if check_result(result, operands)
    )


def check_result(target, operands):
    def calculation(current_value, index):
        # Check result when index has reached end
        if index == len(operands):
            return current_value == target

        # Return all possible operations until index reaches end, combined with "or" only one has to be true to mark
        # the whole equation true.
        next_operand = operands[index]
        return calculation(current_value + next_operand, index + 1) or calculation(current_value * next_operand,
                                                                                   index + 1)

    return calculation(operands[0], 1)


def evaluate_expression(result, operands):
    @cache
    def helper(index, current_value):
        nonlocal result
        if index == len(operands):
            return current_value == result

        next_operand = operands[index]

        # Recursively test addition, multiplication, concatenation
        # Test addition
        if helper(index + 1, current_value + next_operand):
            return True

        # Test multiplication
        if helper(index + 1, current_value * next_operand):
            return True

        # Test concatenation
        concatenated_value = int(str(current_value) + str(next_operand))

        if helper(index + 1, concatenated_value):
            return True

        return False

    return helper(1, operands[0])


def get_sum_equations_with_concetination(equations):
    results = []
    for result, operands in equations:
        if evaluate_expression(result, operands):
            results.append(result)

    return sum(results)


def start_day_challenge(massive_loop=False):
    equations = get_equations()

    # 13. Star
    print(f"13. Sum of solvable equations: {get_sum_equations(equations)}")

    # 14. Star
    if massive_loop:
        print("Total calibration result:", get_sum_equations_with_concetination(equations))
