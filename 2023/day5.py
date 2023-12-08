def timeit(func: callable) -> callable:
    import time

    def time_func():
        start = time.time()
        func()
        end = time.time()
        print(f"Function took {end - start} to execute")

    return time_func

def read_file(path):
    with open(path, "r") as f:
        file = f.read()
    return file

def parse_file(file):
    data = file.strip().split("\n\n")
    header, data = data[0], data[1:]
    data = list(map(lambda x: x.split("\n"), data))
    return header, data

def falls_in_range(source, row_range, seed):
    # print(f"Seed: {seed} with source {source} and range {row_range}")
    return seed >= source and seed <= (source + row_range - 1)

def falls_in_range2(destination, row_range, location):
    return location >= destination and location <= (destination + row_range - 1)

def part_one(header, data):
    locations = []
    for seed in header:
        current_value = seed
        for mapper in data:
            transf_list = list(map(lambda x: x.split(" "), mapper[1:]))
            for row in transf_list:
                row = list(map(int, row))
                destination, source, row_range = row
                if falls_in_range(source, row_range, current_value):
                    current_value = current_value - source + destination
                    break
        locations.append(current_value)
    return locations

def falls_in_seed_range(seed_ranges, seed):
    for min_, max_ in seed_ranges:
        if seed >= min_ and seed <= max_:
            return True
    return False


def part_two(seed_ranges, max_loc, data):
    """
    Check all locations untill you find the good one.
    """
    for location in range(max_loc):
        # print("-"*30, location, "-"*30)
        current_value = location
        for mapper in data:
            # print("IN: ", current_value)
            transf_list = list(map(lambda x: x.split(" "), mapper[1:]))
            # print(transf_list)
            for row in transf_list:
                row = list(map(int, row))
                # print(row)
                destination, source, row_range = row
                if falls_in_range2(destination, row_range, current_value):
                    # print("Inside range!")
                    current_value = current_value - destination + source
                    break
            # print("OUT: ", current_value)
        if falls_in_seed_range(seed_ranges, current_value):
            return location
    
def get_max_loc(data):
    max_loc = max(map(int, (map(lambda x: x.split(" ")[0], data[-1][1:]))))
    return max_loc

@timeit
def main():
    header, data = parse_file(read_file("inputs/day5.txt"))
    # header, data = parse_file(read_file("day5test.txt"))
    # print(data)
    header = list(map(int, list(map(lambda x: x.split(" "), header.split(": ")))[1]))
    locations = part_one(header, data)
    print(min(locations))
    print("-" * 30, " Part Two ", "-"*30)
    seed_ranges = [(header[i], header[i] + header[i+1] - 1) for i in range(0, len(header), 2)]
    max_loc = get_max_loc(data)
    min_loc = part_two(seed_ranges, max_loc, data[::-1])
    print(min_loc)

if __name__ == "__main__":
    main()
    