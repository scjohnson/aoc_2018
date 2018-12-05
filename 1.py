def solution_1(file_name):
    tot = 0
    for line in open(file_name):
        val = int(line)
        tot += val
    return tot

def solution_2(file_name):
    seen = []
    seen.append(0)
    tot = 0
    while True:
        for line in open(file_name):
            val = int(line)
            tot += val
            if tot in seen:
                return tot
            seen.append(tot)


if __name__ == "__main__":
    print("Solution 1: ", solution_1("1.txt"))
    print("Solution 2: ", solution_2("1.txt"))
