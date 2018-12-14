import numpy
import tqdm
import itertools


class Cart():
    def __init__(self):
        self.direction = [0, 0]
        self.position = [0, 0]
        self._turn = "right"

    def set_direction(self, dir):
        if dir == ">":
            self.direction = [1, 0]
        elif dir == "<":
            self.direction = [-1, 0]
        elif dir == "^":
            self.direction = [0, 1]
        elif dir == "v":
            self.direction = [0, -1]

    def turn(self):
        if self._turn == "right":
            self._turn = "left"
            self.direction[0], self.direction[1] =  \
                -self.direction[1], self.direction[0]
        elif self._turn == "straight":
            self._turn = "right"
            self.direction[0], self.direction[1] = self.direction[1], \
                -self.direction[0]
        else:  # turn left
            self._turn = "straight"
        return

    def cmp(self, other):
        if self.position[1] == other.position[1]:
            if self.position[0] < other.position[0]:
                return -1
            else:
                return 1
        elif self.position[1] > other.position[1]:
            return -1
        else:
            return 1

    def __lt__(self, other):
        return self.cmp(other) < 0

    def __gt__(self, other):
        return self.cmp(other) > 0

    def __eq__(self, other):
        return self.cmp(other) == 0

    def __le__(self, other):
        return self.cmp(other) <= 0

    def __ge__(self, other):
        return self.cmp(other) >= 0

    def __ne__(self, other):
        return self.cmp(other) != 0


def read_map(file_name):
    carts = []
    m = []
    j = 0
    for line in open(file_name):
        for i, l in enumerate(line):
            if l == "<" or l == ">" or l == "v" or l == "^":
                cart = Cart()
                cart.set_direction(l)
                cart.position = [i, j]
                carts.append(cart)
        line = line.replace(">", "-")
        line = line.replace("<", "-")
        line = line.replace("^", "|")
        line = line.replace("v", "|")
        line = line.strip("\n")
        m.append(line)
        j += 1
    for cart in carts:
        cart.position[1] = len(m) - cart.position[1] - 1
    m.reverse()
    return m, carts


def crash(carts, y_max, remove_crashes):
    crashed = []
    for (c1, c2) in itertools.combinations(carts, 2):
        if c1.position[0] == c2.position[0] and c1.position[1] == c2.position[1]:
            print("CRASH AT: ", c1.position[0], ",", y_max-c2.position[1] - 1)
            if remove_crashes:
                if c1 not in crashed and c2 not in crashed:
                    crashed.append(c1)
                    crashed.append(c2)
            else:
                return True, carts
    return False, crashed


def propagate(road_map, carts, remove_crashes):
    carts = sorted(carts)
    removed_carts = []
    for cart in carts:
        cart.position = numpy.add(cart.position, cart.direction)
        crashed, crashed_carts = crash(carts, len(road_map), remove_crashes)
        if remove_crashes:
            for cc in crashed_carts:
                removed_carts.append(cc)
        if crashed:
            print("CRASH")
        if road_map[cart.position[1]][cart.position[0]] == "+":
            cart.turn()
        elif road_map[cart.position[1]][cart.position[0]] == "/":
            if cart.direction == [1, 0]:
                cart.direction = [0, 1]
            elif cart.direction == [0, -1]:
                cart.direction = [-1, 0]
            elif cart.direction == [0, 1]:
                cart.direction = [1, 0]
            elif cart.direction == [-1, 0]:
                cart.direction = [0, -1]
        elif road_map[cart.position[1]][cart.position[0]] == "\\":
            if cart.direction == [1, 0]:
                cart.direction = [0, -1]
            elif cart.direction == [0, -1]:
                cart.direction = [1, 0]
            elif cart.direction == [0, 1]:
                cart.direction = [-1, 0]
            elif cart.direction == [-1, 0]:
                cart.direction = [0, 1]
    return removed_carts


def solution_1(file_name, max_steps, remove_crashes=False):
    road_map, carts = read_map(file_name)
    for i in range(max_steps):
        print(i)
        removed_carts = propagate(road_map, carts, remove_crashes)
        print(removed_carts)
        for rm in removed_carts:
            print("removing: ", rm)
            if rm in carts:
                carts.remove(rm)
        print("length: ", len(carts))
        if len(carts) == 1:
            print("LAST AT: ", carts[0].position[0], ",", len(road_map)-carts[0].position[1] - 1)
            return


if __name__ == "__main__":
    # print("Solution 1")
    # print(solution_1("13_test.txt", 16))
    # print("Solution 2")
    # print(solution_1("13_test2.txt", 330))  # 83,49
    # print("Solution 3")
    # print(solution_1("13.txt", 200))  # 115,138
    # print("Solution 4")
    # print(solution_1("13_test2.txt", 30000, True))  # 73,36
    print("Solution 5")
    print(solution_1("13.txt", 300000, True))  #
