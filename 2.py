from collections import Counter
from difflib import SequenceMatcher
from itertools import combinations

def solution_1(file_name):
    twos = 0
    threes = 0
    for line in open(file_name):
        count = Counter(line)
        if 2 in count.values():
            twos +=1
        if 3 in count.values():
            threes +=1
    return twos*threes

def solution_2(file_name):
    lines = []
    for line in open(file_name):
        lines.append(line)
    goal = (len(lines[0])-2.0) / len(lines[0])
    for pairs in combinations(lines, 2):
        ratio = SequenceMatcher(None, pairs[0], pairs[1]).ratio()
        if ratio > goal:
            same = ''
            for i in range(len(pairs[0])):
                if pairs[0][i] == pairs[1][i]:
                    same += pairs[0][i]
            return same


if __name__ == "__main__":
    print("Solution 1: ", solution_1("2.txt")) # 9139
    print("Solution 2: ", solution_2("2.txt")) # uqcidadzwtnhsljvxyobmkfyr
