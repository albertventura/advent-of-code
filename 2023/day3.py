import numpy as np

INPUT_PATH = "inputs/day3.txt"


def read_file(path: str) -> str:
    with open(path, "r") as f:
        file = f.read()
    return file


def timeit(func: callable) -> callable:
    import time

    def time_func():
        start = time.time()
        func()
        end = time.time()
        print(f"Function took {end - start} to execute")

    return time_func


def backtrack_number(row, col, matrix_data, is_right=False):
    upper_limit = matrix_data.shape[1] - 1
    idx = col
    number = ""
    if not is_right:
        while (idx >= 0 and idx <= upper_limit) and matrix_data[row, idx].isdigit():
            idx -= 1
        # You have already entered the while loop so... add one :D
        idx += 1

    while (idx >= 0 and idx <= upper_limit) and matrix_data[row, idx].isdigit():
        current = matrix_data[row, idx]
        number += current
        idx += 1
    return int(number)


def check_adjacent(row, col, matrix_data):
    # look above
    found = []
    if row > 0:
        if matrix_data[row - 1, col].isdigit():
            found.append(backtrack_number(row - 1, col, matrix_data))
            # look upper left diagonal
        else:
            if matrix_data[row - 1, col - 1].isdigit():
                found.append(backtrack_number(row - 1, col - 1, matrix_data))
            # look upper right diagonal
            if matrix_data[row - 1, col + 1].isdigit():
                found.append(backtrack_number(row - 1, col + 1, matrix_data, True))
    # look below
    if row < matrix_data.shape[0]:
        if matrix_data[row + 1, col].isdigit():
            found.append(backtrack_number(row + 1, col, matrix_data))
        else:
            # look lower left diagonal
            if matrix_data[row + 1, col - 1].isdigit():
                found.append(backtrack_number(row + 1, col - 1, matrix_data))
            # look lower right diagonal
            if matrix_data[row + 1, col + 1].isdigit():
                found.append(backtrack_number(row + 1, col + 1, matrix_data, True))
    # look left
    if col > 0:
        if matrix_data[row, col - 1].isdigit():
            found.append(backtrack_number(row, col - 1, matrix_data))

    # look right
    if col < matrix_data.shape[1]:
        if matrix_data[row, col + 1].isdigit():
            found.append(backtrack_number(row, col + 1, matrix_data, True))
    return found


@timeit
def main():
    data = read_file(INPUT_PATH)
    matrix_data = np.array(list(map(lambda x: list(x), data.split("\n"))))
    symbol_idxs = np.where(
        np.logical_and(~np.char.isalnum(matrix_data), matrix_data != ".")
    )
    symbol_idxs = list(zip(symbol_idxs[0], symbol_idxs[1]))
    # print(symbol_idxs)
    # print(matrix_data)
    total = 0
    for row, col in symbol_idxs:
        found = check_adjacent(row, col, matrix_data)
        total += sum(found)
    print(total)

    # part two
    gears_idx = np.where(matrix_data == "*")
    gears_idx = list(zip(gears_idx[0], gears_idx[1]))
    gear_ratios = 0
    for row, col in gears_idx:
        found = check_adjacent(row, col, matrix_data)
        if len(found) == 2:
            gear_ratios += found[0] * found[1]
    print(gear_ratios)


if __name__ == "__main__":
    main()
