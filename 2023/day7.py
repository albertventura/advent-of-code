from collections import Counter
from functools import cmp_to_key


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
    return file.split("\n") 

class Hand:
    def __init__(self, hand, bid, part=1):
        self.hand = hand
        self.bid = int(bid)
        self.counts = Counter(hand)
        if part == 1:
            self.get_type()
        else:
            self.get_strongest_type()
    
    def __str__(self):
        return f"Hand: {self.hand}, Type: {self.type}, Bid: {self.bid}"
    
    def get_type(self):
        if len(self.counts) == 5:
            self.type = "High"
        elif len(self.counts) == 4:
            self.type = "Pair"
        elif len(self.counts) == 3:
            if any(count == 3 for count in self.counts.values()):
                self.type = "Three"
            else:
                self.type = "TwoPair"
        elif len(self.counts) == 2:
            if any(count == 3 for count in self.counts.values()):
                self.type = "Full"
            else:
                self.type = "Four"
        else:
            self.type = "Five"

    def get_strongest_type(self):
        if "J" in self.hand:  
            max_key = None
            for k,v in self.counts.items():
                if k != "J":
                    if not max_key:
                        max_key = k
                    max_key = k if self.counts[k] > self.counts[max_key] else max_key
            self.counts[max_key] += self.counts["J"]
            del self.counts["J"]
        self.get_type()   
   

def build_list_of_hands(data: list[str], part=1) -> list[Hand]:
    return [Hand(play[:5], play[6:], part) for play in data]

def compare_cards(card1, card2):
    # ranks_order = "AKQJT98765432" # Uncomment for part 1
    ranks_order = "AKQT98765432J" # Uncomment for part 2
    return ranks_order.index(card2) - ranks_order.index(card1)

@cmp_to_key
def compare_hands(hand1, hand2):
    for card1, card2 in zip(hand1.hand, hand2.hand):
        if card1 != card2:
            return compare_cards(card1, card2)
    return 0

def sort_hands(data: list[Hand]) -> list[Hand]:
    # bucketize them
    d = {
        "High": [],
        "Pair": [],
        "TwoPair": [],
        "Three": [],
        "Full": [],
        "Four": [],
        "Five": [],
    }
    for h in data:
        d[h.type].append(h)

    sorted_hands = []
    for v in d.values():
        sorted_hands.extend(sorted(v, key=compare_hands,reverse=False))
    return sorted_hands
        

def get_winnings(sorted_hands: list[Hand]) -> int:
    total_winnings = 0
    for i, h in enumerate(sorted_hands):
        total_winnings  += (i + 1) * h.bid
    return total_winnings

@timeit
def main():
    data = parse_file(read_file("inputs/day7.txt"))
    # data = parse_file(read_file("day7test.txt"))
    # # Comment for part 2
    # hands_1 = build_list_of_hands(data)
    # sorted_hands1 = sort_hands(hands_1)
    # total_winnings = get_winnings(sorted_hands1)
    # print(total_winnings)

    # Comment for part 1
    hands_1 = build_list_of_hands(data, part=2)
    sorted_hands1 = sort_hands(hands_1)
    total_winnings = get_winnings(sorted_hands1)
    print(total_winnings)
    
if __name__ == "__main__":
    main()