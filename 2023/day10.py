from copy import deepcopy

pipes = {
    "|": {
        "N": "S",
        "S": "N",
    },
    "-": {
        "W": "E",
        "E": "W",
    },
    "L": {"N": "E", "E": "N"},
    "J": {
        "N": "W",
        "W": "N",
    },
    "7": {"S": "W", "W": "S"},
    "F": {
        "S": "E",
        "E": "S",
    },
}

opposites = {
    "N": "S",
    "S": "N",
    "E": "W",
    "W": "E",
}

def timeit(func: callable) -> callable:
    import time

    def time_func(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"Function took {end - start} to execute")

    return time_func


def read_file(path):
    with open(path, "r") as f:
        file = f.read()
    return file


def parse_file(file):
    return list(map(list, file.splitlines()))


def get_starting_point(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == "S":
                return row, col
    return None


def move(direction, position):
    if direction == "N":
        return (position[0] - 1, position[1])
    elif direction == "S":
        return (position[0] + 1, position[1])
    elif direction == "W":
        return (position[0], position[1] - 1)
    elif direction == "E":
        return (position[0], position[1] + 1)
    else:
        raise Exception("Wrong direction!")


def count_crossing(row, r, c, path_points):
    crossings = 0
    for k in range(c):
        if not (r, k) in path_points:
            continue
        crossings += row[k] in "|JL"
    return crossings


@timeit
def main():
    data = parse_file(read_file("inputs/day10.txt"))
    pos1 = get_starting_point(data)
    pos2 = pos1
    pipetype1 = "|"
    pipetype2 = "|"
    come_from1 = "S"
    come_from2 = "N"
    count = 0
    path_points = set()
    path_points.add(pos1)
    while True:
        if count > 0:
            if pos1 == pos2:
                break

        direction1 = pipes[pipetype1][come_from1]
        come_from1 = opposites[direction1]
        pos1 = move(direction1, pos1)
        pipetype1 = data[pos1[0]][pos1[1]]

        direction2 = pipes[pipetype2][come_from2]
        come_from2 = opposites[direction2]
        pos2 = move(direction2, pos2)
        pipetype2 = data[pos2[0]][pos2[1]]
        count += 1

        path_points.add(pos1)
        path_points.add(pos2)

    print(count)

    print("-" * 30)

    clean_data = deepcopy(data)
    sp = get_starting_point(clean_data)
    clean_data[sp[0]][sp[1]] = "|"
    print(clean_data[sp[0]][sp[1]])
    clean_data = [
        [ch if (i, j) in path_points else "." for j, ch in enumerate(row)]
        for i, row in enumerate(clean_data)
    ]

    result = 0
    for r, row in enumerate(clean_data):
        # print(row)
        for c in range(len(row)):
            if not (r, c) in path_points:
                crossings = count_crossing(row, r, c, path_points)
                if crossings % 2 == 1:
                    result += 1

    print(result)


if __name__ == "__main__":
    main()
