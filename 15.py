import numpy


class Fighter:
    def __init__(self, pos, t, attack=3):
        self.pos = pos
        self.type = t
        self.attack_power = attack
        self.hp = 200
        self.played_round = 0

    def __repr__(self):
        return repr((self.pos[0], self.pos[1]))


def read_map(file_name, elven_attack):
    lines = [line.rstrip('\n') for line in open(file_name)]
    dung_map = numpy.ones([len(lines[0]), len(lines)])
    fighters = []
    for i, line in enumerate(lines):
        for j, l in enumerate(line):
            if l == "#":
                dung_map[j, i] = 0
            elif l == "E":
                fighters.append(Fighter([j, i], 1, attack=elven_attack))
            elif l == "G":
                fighters.append(Fighter([j, i], 0))
    return dung_map, fighters


def calc_distances(defender, fighter, fighters, dungeon_map):
    dest_loc = defender.pos
    distances = numpy.ones(dungeon_map.shape)*10000

    fighter_locations = []
    for f in fighters:
        if f.hp > 0:
            fighter_locations.append(f.pos)

    pot_squares = [
        [dest_loc[0]+1, dest_loc[1]],
        [dest_loc[0]-1, dest_loc[1]],
        [dest_loc[0], dest_loc[1]+1],
        [dest_loc[0], dest_loc[1]-1]]
    distances[dest_loc[0], dest_loc[1]] = 0
    current_dist = 1

    while pot_squares:
        next_pot_squares = []
        for pot_square in pot_squares:
            if distances[pot_square[0], pot_square[1]] > current_dist:
                if (pot_square not in fighter_locations) and (dungeon_map[pot_square[0], pot_square[1]]):
                    distances[pot_square[0], pot_square[1]] = current_dist
                    if distances[pot_square[0], pot_square[1]+1] > current_dist:
                        next_pot_squares.append(
                            [pot_square[0], pot_square[1]+1])
                    if distances[pot_square[0], pot_square[1]-1] > current_dist:
                        next_pot_squares.append(
                            [pot_square[0], pot_square[1]-1])
                    if distances[pot_square[0]+1, pot_square[1]] > current_dist:
                        next_pot_squares.append(
                            [pot_square[0]+1, pot_square[1]])
                    if distances[pot_square[0]-1, pot_square[1]] > current_dist:
                        next_pot_squares.append(
                            [pot_square[0]-1, pot_square[1]])
        current_dist += 1
        pot_squares = next_pot_squares

    # pos_values = []
    # for fighter in fighters:
    #     if fighter != defender:
    min_dist = min(distances[fighter.pos[0]+1, fighter.pos[1]],
                   distances[fighter.pos[0]-1, fighter.pos[1]],
                   distances[fighter.pos[0], fighter.pos[1]+1],
                   distances[fighter.pos[0], fighter.pos[1]-1]) + 1
    # pos_values.append([fighter.pos[0], fighter.pos[1], min_dist])
    # for p in pos_values:
    distances[fighter.pos[0], fighter.pos[1]] = min_dist

    return distances


def calc_move(fighter, distances):
    if distances[fighter.pos[0], fighter.pos[1]] == 1:
        return
    pos = fighter.pos
    pot_positions = []
    pot_positions.append([pos[0]+1, pos[1]])
    pot_positions.append([pos[0]-1, pos[1]])
    pot_positions.append([pos[0], pos[1]+1])
    pot_positions.append([pos[0], pos[1]-1])
    pot_positions = sorted(
        pot_positions, key=lambda p: (p[1], p[0]), reverse=True)
    min_dist = 9999
    for pot_position in pot_positions:
        if distances[pot_position[0], pot_position[1]] <= min_dist:
            fighter.pos = pot_position
            min_dist = distances[pot_position[0], pot_position[1]]


def print_map(dungeon_map, fighters):
    line = ''
    for y in range(0, dungeon_map.shape[1]):
        for x in range(0, dungeon_map.shape[0]):
            if dungeon_map[x, y]:
                line += '.'
            else:
                line += '#'
    l = list(line)
    for f in fighters:
        if f.hp > 0:
            if f.type == 1:
                l[f.pos[0] + f.pos[1]*dungeon_map.shape[0]] = 'E'
            else:
                l[f.pos[0] + f.pos[1]*dungeon_map.shape[0]] = 'G'
    for y in range(0, dungeon_map.shape[1]):
        index = y*dungeon_map.shape[1]
        print(''.join(l[index:index+dungeon_map.shape[0]]))


def purge_fighters(fighters):
    return [f for f in fighters if f.hp > 0]


def currently_fighting(fighters, fight_round):
    return [f for f in fighters if f.played_round < fight_round]


def play_round(dungeon_map, fighters, fight_round):

    fighters = sorted(fighters, key=lambda f: (
        f.pos[1], f.pos[0]), reverse=False)
    while True:
        fighters = purge_fighters(fighters)
        # if they're all the same, the game is won
        types = [f.type for f in fighters if f.hp > 0]
        if all(t == types[0] for t in types):
            return fighters, True

        if not currently_fighting(fighters, fight_round):
            return fighters, False

        fighter = currently_fighting(fighters, fight_round)[0]
        to_attack = []
        min_distance = 9999
        for defender in [f for f in fighters if fighter.type != f.type]:
            dist = calc_distances(defender, fighter, fighters, dungeon_map)[
                fighter.pos[0], fighter.pos[1]]
            if dist <= min_distance:
                if dist == min_distance:
                    to_attack.append(defender)
                else:
                    to_attack = [defender]
                min_distance = dist
        if to_attack:
            to_attack = sorted(
                to_attack, key=lambda f: (f.pos[1], f.pos[0]))
            distances = calc_distances(
                to_attack[0], fighter, fighters, dungeon_map)
            calc_move(fighter, distances)
            list_of_attackees = []
            for defender in fighters:
                if fighter.type != defender.type:
                    if abs(fighter.pos[0]-defender.pos[0])+abs(fighter.pos[1]-defender.pos[1]) == 1:
                        list_of_attackees.append(defender)
            if list_of_attackees:
                list_of_attackees = sorted(list_of_attackees, key=lambda f: (
                    f.hp, f.pos[1], f.pos[0]))
                list_of_attackees[0].hp -= fighter.attack_power
        fighter.played_round += 1


def solution_1(file_name, elven_attack=3):
    dungeon_map, fighters = read_map(file_name, elven_attack)
    print_map(dungeon_map, fighters)

    fight_round = 1
    print("num elves:", len([f for f in fighters if f.type==1]))
    while True:
        fighters, end = play_round(dungeon_map, fighters, fight_round)
        # print_map(dungeon_map, fighters)
        # print(fight_round)
        if end:
            print_map(dungeon_map, fighters)
            print("hp: ", sum([f.hp for f in fighters if f.hp > 0]))
            # print(([f.type for f in fighters if f.hp > 0]))
            # print([f.hp for f in fighters if f.hp > 0])
            print("round: ", fight_round-1)
            print("num elves:", len(fighters))
            return sum([f.hp for f in fighters]) * (fight_round-1)
        fighters = sorted(fighters,
                          key=lambda f: (f.pos[1], f.pos[0]), reverse=False)

        fight_round += 1


if __name__ == "__main__":
    print("Solution")
    # print(solution_1("15_test2.txt"), " =? 27730")
    # print(solution_1("15_test3.txt"), " =? 36334")
    # print(solution_1("15_test4.txt"), " =? 39514")
    # print(solution_1("15_test5.txt"), " =? 27755")
    # print(solution_1("15_test5.txt"), " =? 27755")
    # print(solution_1("15_test6.txt"), " =? 28944")
    # print(solution_1("15.txt"))  # 190012
    # print(solution_1("15_test2.txt", 15), " =? 4988")
    # print(solution_1("15_test4.txt", 4), " =? 31284")
    # print(solution_1("15_test5.txt", 15), " =? 3478")
    # print(solution_1("15_test6.txt", 12), " =? 6474")
    # print(solution_1("15.txt", 8))
    print(solution_1("15.txt", 29)) # 34364
     # 7169, 7236 too low
