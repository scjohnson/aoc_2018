import numpy
import sys
import tqdm
sys.setrecursionlimit(9000)


def fill_map(subpath, area_map, start_loc, length):
    door = 1
    floor = 0
    wall = 2

    current_loc = start_loc[:]
    area_map[tuple(current_loc)] = floor
    while subpath:
        c = subpath[0]
        if c == "E":
            area_map[tuple(current_loc+[1, 0])] = door
            area_map[tuple(current_loc+[2, 0])] = floor
            current_loc = current_loc + [2, 0]
            subpath = subpath[1:]
        elif c == "W":
            area_map[tuple(current_loc+[-1, 0])] = door
            area_map[tuple(current_loc+[-2, 0])] = floor
            current_loc = current_loc + [-2, 0]
            subpath = subpath[1:]
        elif c == "N":
            area_map[tuple(current_loc+[0, 1])] = door
            area_map[tuple(current_loc+[0, 2])] = floor
            current_loc = current_loc + [0, 2]
            subpath = subpath[1:]
        elif c == "S":
            area_map[tuple(current_loc+[0, -1])] = door
            area_map[tuple(current_loc+[0, -2])] = floor
            current_loc = current_loc + [0, -2]
            subpath = subpath[1:]
        elif c == "(":
            subpath, area_map, _ = fill_map(
                subpath[1:], area_map, current_loc, length)
        elif c == '|':
            current_loc = start_loc
            subpath = subpath[1:]
            # subpath, area_map, _ = fill_map(subpath[1:], area_map, start_loc)
        elif c == ")":
            return subpath[1:], area_map, start_loc
        elif c == '$':
            area_map[area_map == -1] = wall
            return '$', area_map, current_loc
    # assert(False)


def distance(area_map, end):
    dists = numpy.ones(area_map.shape, dtype=int) * \
        area_map.shape[0]*area_map.shape[1]
    dists[tuple(end)] = 0
    points = [end]
    while points:
        point = points[0]
        steps = []
        if area_map[tuple(point+[1, 0])] == 1:
            steps.append([2, 0])
        if area_map[tuple(point+[-1, 0])] == 1:
            steps.append([-2, 0])
        if area_map[tuple(point+[0, 1])] == 1:
            steps.append([0, 2])
        if area_map[tuple(point+[0, -1])] == 1:
            steps.append([0, -2])

        for step in steps:
            assert(area_map[tuple(point+step)] == 0)
            if dists[tuple(point+step)] > dists[tuple(point)] + 1:
                dists[tuple(point+step)] = dists[tuple(point)] + 1
                points.append(point+step)

        points = points[1:]
    dists[dists == dists[0][0]] = -1
    return numpy.max(dists), numpy.sum(dists >= 1000)
    # return dists[tuple(start)]


def create_map(path):
    area_map = -1*numpy.ones([len(path)*2, len(path)*2], dtype=int)
    start_point = numpy.array([int(len(path)), int(len(path))], dtype=int)
    _, area_map, _ = fill_map(path[1:], area_map, start_point, len(path[1:]))
    return area_map, start_point


def solution_1(file_name):
    path = [line.rstrip() for line in open(file_name)][0]
    print('creating map')
    area_map, start_point = create_map(path)
    print('calculating distances')
    print(numpy.sum(area_map == 0), "rooms")
    return distance(area_map, start_point)


if __name__ == "__main__":
    print(solution_1("20_test1.txt"), "=? 3")
    print(solution_1("20_test2.txt"), "=? 10")
    print(solution_1("20_test3.txt"), "=? 18")
    print(solution_1("20_test4.txt"), "=? 23")
    print(solution_1("20_test5.txt"), "=? 31")
    print(solution_1("20.txt")) #8351 too low
