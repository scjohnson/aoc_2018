# Solve problem five

def char_combinations():
    for pairs in zip(range(ord('a'), ord('z')+1), range(ord('A'), ord('Z')+1)):
        yield chr(pairs[0])+chr(pairs[1])
        yield chr(pairs[1])+chr(pairs[0])


def react(line):
    line = line.strip()
    while True:
        before = line
        for cc in char_combinations():
            line = line.replace(cc, '')
        if line == before:
            return len(line)


def solution_1(file_name):
    for line in open(file_name):
        line = line.strip()
        return react(line)


def solution_2(file_name):
    for line in open(file_name):
        orig_line = line
        min_size = len(line)
        for rem_cc in char_combinations():
            line = orig_line
            line = line.replace(rem_cc[0], '')
            line = line.replace(rem_cc[1], '')
            current_size = react(line)
            if current_size < min_size:
                min_size = current_size
        return min_size


if __name__ == "__main__":
    print("Solution 1 test: ", solution_1('5_test.txt'), " =? 10")
    print("Solution 1: ", solution_1('5.txt'))  # 9462
    print("Solution 2: ", solution_2('5.txt'))  # 4952
