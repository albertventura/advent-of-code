import re
import math

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
    pattern = re.compile(r'\d+')
    time, distance = file.split("\n")
    time = list(map(int, pattern.findall(time)))
    distance = list(map(int, pattern.findall(distance)))
    return time, distance

def parse_file2(file):
    pattern = re.compile(r'\d+')
    time, distance = file.split("\n")
    time = int("".join(pattern.findall(time)))
    distance = int("".join(pattern.findall(distance)))
    print("time is ", time, "distance is ", distance )
    return time, distance

def get_winning_scenarios(t, d):
    return math.ceil((t + math.sqrt(t ** 2 - 4*d))/2) - math.ceil((t - math.sqrt(t ** 2 - 4*d))/2) 

@timeit
def main():
    time, distance = parse_file(read_file("inputs/day6.txt"))
    # time, distance = parse_file(read_file("day6test.txt"))
    print(time, distance)
    total_scenarios = 1
    for t, d in zip(time, distance):
        total_scenarios *= get_winning_scenarios(t, d)
    print(total_scenarios)
    time, distance = parse_file2(read_file("inputs/day6.txt"))
    total_scenarios = get_winning_scenarios(time, distance)
    print(total_scenarios)

if __name__ == '__main__':
    main()