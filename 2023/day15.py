from collections import defaultdict

def read_file(path):
    with open(path, "r") as f:
        file = f.read()
    return file

def hash_step(ch, current_value=0):
    current_value += ord(ch) 
    current_value *=  17
    current_value = current_value % 256
    return current_value

def run_hash(s):
    current_value = 0
    for ch in s:
        current_value = hash_step(ch, current_value)
    return current_value

def dash_operation(step, boxes):
    label = step[:len(step) - 1]
    hashed_label = run_hash(label)
    lenses = boxes.get(hashed_label, [])
    if lenses:
        for lens in lenses:
            if label in lens:
                boxes[hashed_label] = [lens for lens in lenses if label not in lens]
                break

def equal_operation(step, boxes):
    label, f = step.split("=")
    hashed_label = run_hash(label)
    value = step.replace("=", " ")
    lenses = boxes.get(hashed_label, [])
    if lenses:
        new_lenses = []
        sub = False
        for lens in lenses:
            if label in lens:
                new_lenses.append(value)
                sub = True
            else:
                new_lenses.append(lens)
        if not sub:
            new_lenses.append(value)
        boxes[hashed_label] = new_lenses
    else:
        boxes[hashed_label].append(value)
    
def main():
    # file = read_file("day15test.txt")
    file = read_file("inputs/day15.txt")
    total = 0
    for val in file.replace("\n", "").split(","):
        total += run_hash(val)
    print(total)

    boxes = defaultdict(list)
    for step in file.replace("\n", "").split(","):
        if "=" in step:
            equal_operation(step, boxes)
        elif "-" in step:
            dash_operation(step, boxes)
        else:
            raise Exception("Wrong operation!")


    focusing_power = 0
    for k,v in boxes.items():
        for i, el in enumerate(v):
            focusing_power += (k + 1) * (i + 1) * int(el[-1])
    print(focusing_power)

if __name__ == "__main__":
    main()
    