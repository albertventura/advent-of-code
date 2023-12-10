import numpy as np 
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

def parse_file(file):
    lines = file.split('\n')
    result = []
    for line in lines:
        numbers = re.findall(r'-?\d+', line)
        if numbers:
            result.append([int(num) for num in numbers])

    return result

def difference_sequence(seq: list) -> list:
    return [seq[i + 1] -  seq[i] for i in range(0, len(seq) - 1)]

def extrapolate(seq):
    end_num = []
    while any(seq):
        end_num.append(seq[-1])
        seq = difference_sequence(seq)
    return np.cumsum(end_num)[-1]

    

@timeit
def main():
    data = parse_file(read_file("inputs/day9.txt"))
    # data = parse_file(read_file("day9test.txt"))
    sum_extrapolated = 0
    sum_p2 = 0
    for seq in data:
        sum_extrapolated += extrapolate(seq)
        sum_p2 += extrapolate(seq[::-1]) 
    print(sum_extrapolated)
    print(sum_p2)

if __name__ == "__main__":
    main()