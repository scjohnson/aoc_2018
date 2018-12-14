# Smlve problem six
import numpy
from itertools import product


def man_dist(c1, c2):
    return abs(c1[0]-c2[0]) + abs(c1[1]-c2[1])


def solution_1(file_name, max_tot_dist):
    coords = []
    for line in open(file_name):
        coord = line.split(',')
        coord = (int(coord[0]), int(coord[1]))
        coords.append(coord)
    maxx = max([x[0] for x in coords]) + 1
    maxy = max([x[1] for x in coords]) + 1
    grid = numpy.zeros((maxx, maxy))
    for i, j in product(range(maxx), range(maxy)):
        min_dist = maxx + maxy + 1
        for idx, coord in enumerate(coords):
            dist = man_dist((i, j), coord)
            if dist == min_dist:
                grid[i, j] = -1
            elif dist <= min_dist:
                grid[i, j] = idx
                min_dist = dist

    max_total = 0
    unsafe = []
    for idx, _ in enumerate(coords):
        if not ((numpy.any(grid[:, maxy-1] == idx)) or
                (numpy.any(grid[:, 0] == idx)) or
                (numpy.any(grid[maxx - 1, :] == idx)) or
                (numpy.any(grid[0, :] == idx))):
            total = sum(sum(grid == idx))
            if total > max_total:
                max_total = total
        else:
            unsafe.append(idx)

    for i, j in product(range(maxx), range(maxy)):
        min_dist = maxx + maxy + 1
        idxs = []
        for idx, coord in enumerate(coords):
            dist = man_dist((i, j), coord)
            if dist == min_dist:
                idxs.append(idx)
            elif dist < min_dist:
                grid[i, j] = idx
                min_dist = dist
                idxs = []
                idxs.append(idx)

    for i, j in product(range(maxx), range(maxy)):
        if grid[i, j] != max_tot_dist:
            dist = 0
            for idx, coord in enumerate(coords):
                dist += man_dist(coord, (i, j))
            grid[i, j] = dist
    size = sum(sum(grid < max_tot_dist))

    return max_total, size


if __name__ == "__main__":
    print("Solution 1 test: ", solution_1('6_test.txt', 32), " =? 17, 16")
    print("Solution 1 & 2: ", solution_1('6.txt', 10000))  # 3894, 39398
