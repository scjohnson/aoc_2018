import numpy
import tqdm


def calc_next_state(current_state, rules, zero):
    next_state = []
    for i, _ in enumerate(current_state):
        little_state = current_state[max(
            [i-2, 0]):min([i+3, len(current_state)])]
        if i == 1:
            little_state = [0] + little_state
        elif i == 0:
            little_state = [0, 0] + little_state
        elif i == len(current_state) - 1:
            little_state.append(0)
            little_state.append(0)
        elif i == len(current_state) - 2:
            little_state.append(0)
        if tuple(little_state) in rules:
            next_state.append(1)
        else:
            next_state.append(0)
    if sum(next_state[0:2]) > 0:
        next_state = [0, 0] + next_state
        zero += 2
    if sum(next_state[-2:]) > 0:
        next_state.append(0)
        next_state.append(0)
    return next_state, zero


def convert(text):
    out = []
    for i, val in enumerate(text.strip()):
        if val == '#':
            out.append(1)
        else:
            out.append(0)
    return out


def solution_1(file_name, num_generations):
    initial_state = []
    rules = {}
    for line in open(file_name):
        if initial_state == []:
            initial_state = convert(line.split(":")[1])
            initial_state = [0, 0] + initial_state + [0, 0]
        else:
            line = line.split(" ")
            if (sum(convert(line[2]))) > 0:
                rules[tuple(convert(line[0]))] = convert(line[2])

    zero = 2
    states = []
    current_state = initial_state
    tot = 0
    prev_tot = 0
    for i in tqdm.tqdm(range(num_generations)):
        current_state, zero = calc_next_state(current_state, rules, zero)
        tot = 0
        for j, val in enumerate(current_state):
            if val == 1:
                tot += j - zero
        print(i, tot, tot-prev_tot, (50000000000 - i - 1) * (tot-prev_tot) + tot)
        prev_tot = tot
    return tot


if __name__ == "__main__":
    print(solution_1("12_test.txt", 20))
    print(solution_1("12.txt", 20))  # 1787
    print(solution_1("12.txt", 50000000000)) # 1100000000475
