import numpy
import tqdm


def read_data(file_name):
    lines = [line.rstrip() for line in open(file_name)]
    area = numpy.zeros([len(lines[0]), len(lines)])
    for j, line in enumerate(lines):
        for i, c in enumerate(line):
            if c == '.':
                area[i, j] = 0
            elif c == '|':
                area[i, j] = 1
            else:
                area[i, j] = 2
    return area


def evolve(area):
    new_area = numpy.zeros(area.shape)
    for i in range(area.shape[0]):
        for j in range(area.shape[1]):
            # if open
            if area[i, j] == 0:
                num_trees = 0
                for il in range(max(i-1, 0), min(i+2, area.shape[0])):
                    for jl in range(max(j-1, 0), min(j+2, area.shape[1])):
                        if area[il, jl] == 1 and not (il == i and jl == j):
                            num_trees += 1
                if num_trees > 2:
                    new_area[i, j] = 1
                else:
                    new_area[i, j] = 0
            # if trees
            elif area[i, j] == 1:
                num_lumber = 0
                for il in range(max(i-1, 0), min(i+2, area.shape[0])):
                    for jl in range(max(j-1, 0), min(j+2, area.shape[1])):
                        if area[il, jl] == 2. and not (il == i and jl == j):
                            num_lumber += 1
                if num_lumber > 2:
                    new_area[i, j] = 2
                else:
                    new_area[i, j] = 1
            else:
                num_lumber = 0
                num_trees = 0
                for il in range(max(i-1, 0), min(i+2, area.shape[0])):
                    for jl in range(max(j-1, 0), min(j+2, area.shape[1])):
                        if area[il, jl] == 2 and not (il == i and jl == j):
                            num_lumber += 1
                        if area[il, jl] == 1 and not (il == i and jl == j):
                            num_trees += 1
                if num_lumber > 0 and num_trees > 0:
                    new_area[i, j] = 2
                else:
                    new_area[i, j] = 0
    return new_area


def score(area):
    return numpy.sum(area == 1)*numpy.sum(area == 2)


def solution_1(file_name, minutes):
    area = read_data(file_name)
    for i in (range(minutes)):
        area = evolve(area)
        if (minutes-i-1) % 56 == 0:
            print(i, score(area))
    return score(area)


if __name__ == "__main__":
    print("Solution")
    print(solution_1("18_test.txt", 10))
    print(solution_1("18.txt", 10))
    print(solution_1("18.txt", 1000000000), " ?= 169106")
