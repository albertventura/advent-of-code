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


def find_all_galaxies(s, row, empty_cols, dilation_factor):
    positions = []
    index = s.find("#")
    while index != -1:
        expansion_factor = len(list(filter(lambda x: x < index, empty_cols))) 
        # This was hard.. For each column that I duplicate I need to substract that same column
        expansion_factor = expansion_factor * dilation_factor - expansion_factor
        positions.append((row, index + expansion_factor))
        index = s.find("#", index + 1)
    return positions


def transpose_string(s):
    transposed_list = list(zip(*list(map(list, s.split()))))
    return "\n".join(["".join(row) for row in transposed_list])


def parse_file(f, dilation_factor=1):
    tf = transpose_string(f)
    empty_cols = []
    galaxies = []
    for i, col in enumerate(tf.splitlines()):
        if all(char == "." for char in col):
            empty_cols.append(i)
    j = 0
    for line in f.splitlines():
        galaxies_in_line = find_all_galaxies(line, j, empty_cols, dilation_factor)
        if not galaxies_in_line:
            j += 1 * dilation_factor - 1
        galaxies.extend(galaxies_in_line)
        j += 1
    return galaxies


@timeit
def main():
    galaxies = read_file("inputs/day11.txt")
    # galaxies = read_file("day11test.txt")
    galaxies1 = parse_file(galaxies)
    distances1 = [
        abs(y[0] - x[0]) + abs(y[1] - x[1])
        for i, x in enumerate(galaxies1)
        for j, y in enumerate(galaxies1)
        if i < j
    ]
    print(sum(distances1))

    galaxies2 = parse_file(galaxies, dilation_factor=1_000_000)
    distances2 = [
        abs(y[0] - x[0]) + abs(y[1] - x[1])
        for i, x in enumerate(galaxies2)
        for j, y in enumerate(galaxies2)
        if i < j
    ]
    print(sum(distances2))

if __name__ == "__main__":
    main()
