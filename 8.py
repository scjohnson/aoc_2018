# Solve problem six
import numpy
from itertools import product

def read_element(line, index):
    num_nodes = line[index]
    entries = line[index+1]
    index += 2
    total = 0
    for i in range(num_nodes):
        index, t = read_element(line, index)
        total += t
        
    for i in range(entries):
        total += line[index+i]
    index += entries
    return index, total


def solution_1(file_name):
    f = open(file_name)
    line = f.read()
    line = [int(l) for l in line.split(' ')]
    _, total = read_element(line, 0)
    return total


def read_element_weighted(line, index):
    num_nodes = line[index]
    entries = line[index+1]
    index += 2
    totals = []
    for i in range(num_nodes):
        index, t = read_element_weighted(line, index)
        totals.append(t)

    total = 0
    if num_nodes == 0:
        for i in range(entries):
            total += line[index+i]
    else:
        for i in range(entries):
            if line[index+i] <= num_nodes:
                total += totals[line[index+i]-1]
    index += entries
    return index, total

def solution_2(file_name):
    f = open(file_name)
    line = f.read()
    line = [int(l) for l in line.split(' ')]
    _, total = read_element_weighted(line, 0)
    return total


if __name__ == "__main__":
    print("Solution 1 test: ", solution_1('8_test.txt'), " =? 138")
    print("Solution 1: ", solution_1('8.txt')) # 38567
    print("Solution 2 test: ", solution_2('8_test.txt'), " =? 66")
    print("Solution 2 test: ", solution_2('8.txt'))  #24453
