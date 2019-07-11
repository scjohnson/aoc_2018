import numpy
spring = [500, 0]


def read_data(file_name):
    lines = [line.rstrip() for line in open(file_name)]
    clay_x = []
    clay_y = []
    for line in lines:
        line = line.split(",")
        position = line[0].split("=")[1]
        clay_line = line[1].split("..")
        clay_line[0] = clay_line[0].split("=")[1]
        if line[0][0] == 'x':
            clay_x.append([position, clay_line])
        else:
            clay_y.append([position, clay_line])

    min_x = 1e9
    min_y = 1e9
    max_x = 0
    max_y = 0
    for line in clay_x:
        max_x = max(max_x, int(line[0]))
        min_x = min(min_x, int(line[0]))
        max_y = max(max_y, int(line[1][0]))
        min_y = min(min_y, int(line[1][1]))
    for line in clay_y:
        max_y = max(max_y, int(line[0]))
        min_y = min(min_y, int(line[0]))
        max_x = max(max_x, int(line[1][0]))
        min_x = min(min_x, int(line[1][1]))
    max_x += 1
    max_y += 1
    min_x -= 1
    min_y -= 1

    area = numpy.zeros([max_x, max_y], dtype=int)
    for cx in clay_x:
        area[int(cx[0]), int(cx[1][0]):int(cx[1][1])+1] = 1
    for cy in clay_y:
        area[int(cy[1][0]):int(cy[1][1])+1, int(cy[0])] = 1

    # print(area[494:508, 0:14].transpose())
    return area


def propagate(area, sources, fills, priors):

    while sources:
        source = sources[0]
        i = source[0]
        j = source[1] + 1
        while j < area.shape[1]-1:
            area[i][j] = 2
            if area[i][j+1] != 0:
                break
            j += 1
        if j < area.shape[1]-1:
            if area[i][j+1] == 2:
                fills.append([i, j+1])
            else:
                fills.append([i, j])

        else:
            area[i][j] = 2
        priors.append(source)
        sources.pop(0)

    while fills:
        created_sources = False
        fill = fills[0]

        i = fill[0]
        j = fill[1]
        # look to the right
        while i < area.shape[0]-1:
            area[i, j] = 2
            if [i, j] in priors:
                break
            if area[i+1][j] == 1 or area[i][j+1] == 0:
                break
            i += 1
        if area[i][j+1] == 0:
            if [i, j] not in priors:
                sources.append([i, j])
            created_sources = True

        i = fill[0]
        j = fill[1]
        # look to the left
        while i >= 0:
            area[i, j] = 2
            if [i, j] in priors:
                break
            if area[i-1][j] == 1 or area[i][j+1] == 0:
                break
            i -= 1
        if area[i][j+1] == 0:
            if [i, j] not in priors:
                sources.append([i, j])
            created_sources = True

        if not created_sources:
            fills.append([fill[0], fill[1]-1])

        fills.pop(0)

    return area, sources, fills, priors


def solution_1(file_name):
    area = read_data(file_name)
    # print(area.T)
    sources = [spring]
    fills = []
    prior = []
    # print(area[494:508, 0:14].transpose())
    i = 0
    while sources or fills:
        # print(sources)
        # print(fills)
        (area, sources, fills, prior) = propagate(area, sources, fills, prior)
        # print(area[494:508, 0:14].transpose())
        numpy.savetxt("17-"+str(i)+".csv", area.transpose(), delimiter=',')
        i += 1
    return numpy.sum(area == 2)
    # print(area.T)


if __name__ == "__main__":
    print("Solution")
    print(solution_1("17_test.txt"), " =? 57")
    print(solution_1("17.txt"))  # 2906/2907 too low
