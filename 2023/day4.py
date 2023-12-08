INPUT_PATH = "inputs/day4.txt"

def timeit(func: callable) -> callable:
    import time

    def time_func():
        start = time.time()
        func()
        end = time.time()
        print(f"Function took {end - start} to execute")

    return time_func


def read_file(file_path):
    with open(file_path, "r") as f:
        data = f.read()
    return data


def parse_file(file):
    file = file.strip().split("\n")
    file = list(map(lambda x: x.replace("  ", " "), file))
    file = list(map(lambda x: x.strip().split(": ")[1], file))
    file = list(map(lambda x: x.strip().split(" | "), file))
    file = list(
        map(
            lambda x: (
                list(map(int, x[0].strip().split(" "))),
                list(map(int, x[1].strip().split(" "))),
            ),
            file,
        )
    )
    return file


def get_total_scratchcards(data: list):
    amount_of_cards = [1 for el in data]
    for idx, extras in enumerate(data):
        for i in range(idx + 1, idx + extras + 2):
            amount_of_cards[i] += amount_of_cards[idx]
    return sum(amount_of_cards)


@timeit
def main():
    data = parse_file(read_file(INPUT_PATH))
    part_one = [
        2 ** (len(set(winner).intersection(set(owned))) - 1)
        if 2 ** (len(set(winner).intersection(set(owned))) - 1) >= 1
        else 0
        for winner, owned in data
    ]
    print(sum(part_one))
    part_two_data = [
        (len(set(winner).intersection(set(owned))) - 1) for winner, owned in data
    ]
    print(get_total_scratchcards(part_two_data))


if __name__ == "__main__":
    main()
