import numpy
import tqdm
import itertools


def get_recipies(recipies, elf_locations):
    tot = 0
    for elf in elf_locations:
        tot += recipies[elf]
    new_rec = str(tot)
    return [int(x) for x in new_rec]


def solution_1(num_recipies):

    recipies = [3, 7]
    elf_locations = [0, 1]

    while len(recipies) < num_recipies + 10:
        recipies.extend(get_recipies(recipies, elf_locations))
        new_locs = []
        for elf in elf_locations:
            new_locs.append((1 + elf + recipies[elf]) % len(recipies))
        elf_locations = new_locs
    score = ''
    for i in recipies[num_recipies:num_recipies+10]:
        score += str(i)
    return score


def solution_2(value):

    recipies = [3, 7]
    elf_locations = [0, 1]

    while True:
        new_recipies = get_recipies(recipies, elf_locations)
        recipies.extend(new_recipies)
        new_locs = []
        for elf in elf_locations:
            new_locs.append((1 + elf + recipies[elf]) % len(recipies))
        elf_locations = new_locs
        for i in range(len(new_recipies)):
            index = len(recipies) - len(value) - i
            if recipies[index:index+len(value)] == value:
                return index


if __name__ == "__main__":
    print("Solution 1")
    print(solution_1(9), "=? 5158916779")
    print(solution_1(2018), "=? 5941429882")
    print(solution_1(793031))
    print(solution_2([5, 1, 5, 8, 9]), "=? 9")
    print(solution_2([5, 9, 4, 1, 4]), "=? 2018")
    print(solution_2([7, 9, 3, 0, 3, 1]))
