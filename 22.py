import numpy


def calc_gindex(target):
    gindex = numpy.zeros([target[0]+1, target[1]+1])
    gindex[0, 0] = 0
    gindex[tuple(target)] = 0
    for i in range(gindex.shape[0]):
        gindex[i, 0] = i*16807
    for i in range(gindex.shape[1]):
        gindex[0, i] = i*48271
    for i, j in zip(range(gindex.shape[0]), range(gindex.shape[1])):
        i, j

# Otherwise, the region's geologic index is the result of multiplying the erosion levels of the regions at X-1, Y and X, Y-1.


def solution_1(start_depth, target):
    calc_gindex(target)
    area = numpy.zeros(target)
    print(area)
    return

# 0 for rocky regions, 1 for wet regions, and 2 for narrow regions.


if __name__ == "__main__":
    print(solution_1(510, [10, 10]), "=? 114")
    # print(solution_1(7305, [13, 734]), "=? 114")
