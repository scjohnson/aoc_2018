# Solve problem six
import numpy
from itertools import product


def solution_1(file_name):
    dirs = {}
    values = set([])
    for line in open(file_name):
        line = line.split(' ')
        first, second = line[1], line[7]
        values.add(first)
        values.add(second)
        if first in dirs:
            dirs[first].append(second)
        else:
            dirs[first] = [second]
    ordered_list = []
    while dirs:
        pointed_to = set([])
        for k, pt in dirs.items():
            for p in pt:
                pointed_to.add(p)
        not_pointed_to = values-pointed_to
        npt = list(not_pointed_to)
        npt.sort()
        next_value = npt[0]
        ordered_list.append(next_value)
        if len(dirs) == 1:
            last = dirs[next_value][0]
            ordered_list.append(last)
        dirs.pop(next_value, None)
        values.remove(next_value)

    return ''.join(ordered_list)


class Worker():
    working = ''
    time_left = 0


def solution_2(file_name, num_workers, time_offset):
    dirs = {}
    values = set([])
    for line in open(file_name):
        line = line.split(' ')
        first, second = line[1], line[7]
        values.add(first)
        values.add(second)
        if first in dirs:
            dirs[first].append(second)
        else:
            dirs[first] = [second]

    secs = 0
    workers = []
    for _ in range(num_workers):
        workers.append(Worker())

    while True:
        for worker in workers:
            if worker.working:
                worker.time_left -= 1

        free_workers = []

        for worker in workers:
            if worker.time_left == 0:
                free_workers.append(worker)
                if worker.working:
                    dirs.pop(worker.working, None)
                if len(dirs) == 1:
                    if next_value in dirs:
                        if len(dirs[next_value]) == 1:
                            dirs[dirs[next_value][0]] = []
                worker.working = ''

        if len(free_workers) == num_workers and len(dirs) == 0:
            return secs

        for idx, worker in enumerate(free_workers):
            pointed_to = set([])
            for k, pt in dirs.items():
                for p in pt:
                    pointed_to.add(p)
            not_pointed_to = values-pointed_to
            npt = list(not_pointed_to)
            npt.sort()
            if npt:
                next_value = npt[0]
                worker.working = next_value
                worker.time_left = ord(next_value)-ord('A') + 1 + time_offset
                values.remove(worker.working)

        secs += 1


if __name__ == "__main__":
    print("Solution 1 test: ", solution_1('7_test.txt'), " =? CABDFE")
    print("Solution 1: ", solution_1('7.txt'))
    print("Solution 2 test: ", solution_2('7_test.txt', 2, 0), " =? 15")
    print("Solution 2 test: ", solution_2('7.txt', 5, 60))  # 253, 254 too low
