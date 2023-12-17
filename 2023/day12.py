import re

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

def is_valid(seq, constraints):
    groups = re.findall(r"\#+", seq)
    if len(groups) != len(constraints):
        return False
    elif list(map(len, groups)) != constraints:
        return False
    return True

def find_combinations(seq, constraints, i):
    if i == len(seq):
        return 1 if is_valid(seq, constraints) else 0
    if seq[i] == "?":
        return (
            find_combinations(seq[:i] + "#" + seq[i + 1:], constraints, i + 1)
            + find_combinations(seq[:i] + "." + seq[i + 1:], constraints, i + 1)
        )
    else:
        return find_combinations(seq, constraints, i + 1)
    

@timeit
def main():
    # data = read_file("day12test.txt")
    data = read_file("inputs/day12.txt")
    total = 0
    for line in data.splitlines():
        seq, constraints = line.split(" ")
        constraints = list(map(int, constraints.split(",")))
        total += find_combinations(seq, constraints, 0)
    print(total)

if __name__ == "__main__":
    main()