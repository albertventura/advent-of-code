import numpy as np

def read_file(path):
    with open(path, "r") as f:
        file = f.read()
    return file

def move_column_rocks(col):
    # print("before\n", col)
    col_load = 0
    C = len(col)
    for i in range(C):
        if col[i] == "O":
            if i == 0:
                col_load += C
                continue
            j = i
            while col[j - 1] == "." and j > 0:
                col[j - 1], col[j] = col[j], col[j - 1]
                j -= 1

def move_rocks(matrix):
    for col in range(matrix.shape[1]):
        column = matrix[:, col]
        move_column_rocks(column)

def compute_load(matrix):
    load = 0
    C = matrix.shape[1]
    for col in range(matrix.shape[1]):
        for i, el in enumerate(matrix[:, col]):
            if el == "O":
                load += C - i
    return load

def main():
    # data = read_file("day14test.txt")
    data = read_file("inputs/day14.txt")
    matrix = np.array(list(map(list, data.split("\n"))))
    move_rocks(matrix)

    print("Total Load: ", compute_load(matrix))
    print("-" * 30 , "PART TWO", "-" * 30)
    
    matrix = np.array(list(map(list, data.split("\n"))))
    cache = {}
    cycle = 0
    n_cycles = 1_000_000_000
    while True:
        for _ in range(4):
            move_rocks(matrix)
            matrix = np.rot90(matrix, k = 3)

        hashable_matrix = tuple(tuple(row) for row in matrix)
        if hashable_matrix in cache:
            period = cycle - cache[hashable_matrix]
            print(cycle)
            break

        cache[hashable_matrix] = cycle
        cycle += 1

    dif = cycle - period
    idx = (n_cycles - 1 - dif) % period + dif # Number of cycles completed before repeating, considering adjustments for n_cycles
    for mat, i in cache.items():
        if i == idx:
            matrix = np.array(mat)
            total = compute_load(matrix)
            break
    print(total)
if __name__ == "__main__":
    main()

