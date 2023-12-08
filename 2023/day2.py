INPUT_PATH = "./inputs/day2.txt"
LIMIT_RED = 12
LIMIT_GREEN = 13
LIMIT_BLUE = 14


def timeit(func: callable) -> callable:
    import time

    def time_func():
        start = time.time()
        func()
        end = time.time()
        print(f"Function took {end - start} to execute")

    return time_func


def is_possible(num, color):
    if color == "green":
        return False if num > LIMIT_GREEN else True
    elif color == "blue":
        return False if num > LIMIT_BLUE else True
    elif color == "red":
        return False if num > LIMIT_RED else True
    else:
        raise Exception("unexpected color")


def decompose_line(line: str):
    line = line.split(":")
    game_num, events = int(line[0].split()[1]), line[1]
    # print(value, events)
    events = events.replace(";", ",").split(",")
    events = list(map(lambda x: x.strip().split(), events))
    return game_num, events

@timeit
def main():
    result = []
    total_power = 0
    with open(INPUT_PATH, "r") as f:
        for line in f:
            game_num, events = decompose_line(line)
            possible = True
            d_mins = {}
            for num, color in events:
                num = int(num)
                if not d_mins.get(color, None):
                    d_mins[color] = num
                else:
                    if d_mins[color] < num:
                        d_mins[color] = num
                if not possible:
                    continue
                possible = is_possible(num, color)
            power = 1
            for v in d_mins.values():
                power *= v
            total_power += power
    print(sum(result))
    print(total_power)


if __name__ == "__main__":
    main()
