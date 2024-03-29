import re
import math

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
    sps = re.findall(r"([A-Z]{2}A)\s=", file)
    print(sps)
    return instructions[0], d, sps

@timeit
def main():
    instructions, maps, sps = parse_file(read_file("inputs/day8.txt"))
    # instructions, maps, sps = parse_file(read_file("day8test.txt"))
    print("SPS ", sps)
    i = 0
    sp = "AAA"

    while sp != "ZZZ":
        ins = instructions[i % len(instructions)]
        # print("Current point: ", sp)
        # print("Instructed to go: ", ins)
        sp = maps[sp][0 if ins == "L" else 1]
        i+=1
    print(i)

    # Part two
    steps = []
    for sp in sps:
        j = 0
        while not sp[-1] == "Z":
            ins = instructions[j % len(instructions)]
            sp = maps[sp][0 if ins == "L" else 1]
            j +=1
        steps.append(j)
        print("Finished one")
    print(math.lcm(*steps))    

if __name__ == "__main__":
    main()
    

