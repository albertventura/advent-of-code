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
    ins_pattern = r"[RL]+(?=\n)"
    map_pattern = r"([A-Z]{3})\s=\s\(([^)]+)\)"
    instructions = re.findall(ins_pattern, file)
    d = {el[0]: el[1].split(", ") for el in re.findall(map_pattern, file)}
    # print(d)
    return instructions[0], d


@timeit
def main():
    instructions, maps = parse_file(read_file("inputs/day8.txt"))
    # instructions, maps = parse_file(read_file("day8test.txt"))
    print(instructions)
    i = 0
    sp = "AAA"
    while sp != "ZZZ":
        ins = instructions[i % len(instructions)]
        # print("Current point: ", sp)
        # print("Instructed to go: ", ins)
        sp = maps[sp][0 if ins == "L" else 1]
        i+=1
    
    print(i)

if __name__ == "__main__":
    main()
    

