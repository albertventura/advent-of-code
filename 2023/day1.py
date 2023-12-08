INPUT_PATH = "inputs/day1.txt"
MAPPER = {
    "zero": "z0o",
    "one":"o1e",
    "two":"t2o",
    "three":"t3e",
    "four": "f4r",
    "five": "f5e", 
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
}

def timeit(func: callable) -> callable:
    import time
    def time_func():
        start = time.time() 
        func()
        end = time.time()
        print(f"Function took {end - start} to execute")
    return time_func

def read_file(path: str) -> str:
    with open(path, "r") as f:
        file = f.read()
    return file

def replace_dict(callibration: str, mapper: dict=MAPPER) -> str:
    for k,v in mapper.items():
        callibration = callibration.replace(k, v)
    return callibration

def parse_file(data: str) -> list[str]:
    return data.split("\n")

def get_callibration(callibration: str) -> int:
    first = None
    last = None
    for char in callibration:
        if char.isdigit():
            if not first:
                first = char
            last = char
    return int(first+last)

@timeit
def main():
    data = parse_file(read_file(INPUT_PATH))
    print("PART ONE:\n The total callibration is: ", sum(map(get_callibration, data)))
    print("PART TWO: ")
    print("The new total callibration is: ", sum(map(get_callibration, map(replace_dict, data))))

if __name__ == '__main__':
    main()