import numpy as np

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


@timeit
def main():
    data = read_file("day13test.txt")
    samples = [np.array(list(map(list, pattern.split("\n")))) for pattern in data.split("\n\n")]
    
    

if __name__ == "__main__":
    main()