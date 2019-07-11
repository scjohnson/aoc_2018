import re
import tqdm
import numpy


def addr(registers, A, B, C):
    ans = registers[::]
    ans[C] = registers[A] + registers[B]
    return ans


def addi(registers, A, B, C):
    ans = registers[::]
    ans[C] = registers[A] + B
    return ans


def mulr(registers, A, B, C):
    ans = registers[::]
    ans[C] = registers[A] * registers[B]
    return ans


def muli(registers, A, B, C):
    ans = registers[::]
    ans[C] = registers[A] * B
    return ans


def banr(registers, A, B, C):
    ans = registers[::]
    ans[C] = registers[A] & registers[B]
    return ans


def bani(registers, A, B, C):
    ans = registers[::]
    ans[C] = registers[A] & B
    return ans


def borr(registers, A, B, C):
    ans = registers[::]
    ans[C] = registers[A] | registers[B]
    return ans


def bori(registers, A, B, C):
    ans = registers[::]
    ans[C] = registers[A] | B
    return ans


def setr(registers, A, B, C):
    ans = registers[::]
    ans[C] = registers[A]
    return ans


def seti(registers, A, B, C):
    ans = registers[::]
    ans[C] = A
    return ans


def gtir(registers, A, B, C):
    ans = registers[::]
    if A > registers[B]:
        ans[C] = 1
    else:
        ans[C] = 0
    return ans


def gtri(registers, A, B, C):
    ans = registers[::]
    if registers[A] > B:
        ans[C] = 1
    else:
        ans[C] = 0
    return ans


def gtrr(registers, A, B, C):
    ans = registers[::]
    if registers[A] > registers[B]:
        ans[C] = 1
    else:
        ans[C] = 0
    return ans


def eqir(registers, A, B, C):
    ans = registers[::]
    if A == registers[B]:
        ans[C] = 1
    else:
        ans[C] = 0
    return ans


def eqri(registers, A, B, C):
    ans = registers[::]
    if registers[A] == B:
        ans[C] = 1
    else:
        ans[C] = 0
    return ans


def eqrr(registers, A, B, C):
    ans = registers[::]
    if registers[A] == registers[B]:
        ans[C] = 1
    else:
        ans[C] = 0
    return ans


operations = [addr, addi, mulr, muli, banr, bani, borr, bori,
              setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]


def read_before_after(line):
    res = re.split('\W+', line.split('[')[1])[0:4]
    return [int(r) for r in res]


def solution_1(file_name):
    lines = [line.rstrip('\n') for line in open(file_name)]
    tot = 0
    pot_ops = {}
    for i, line in enumerate(lines):
        if line[0:7] == "Before:":
            before = read_before_after(line)
            op = re.split('\W+', lines[i+1])[0:4]
            op = [int(o) for o in op]
            after = read_before_after(lines[i+2])
            num = 0
            for index, operation in enumerate(operations):
                if operation(before, op[1], op[2], op[3]) == after:
                    if op[0] not in pot_ops:
                        pot_ops[op[0]] = []
                    pot_ops[op[0]].append(index)
                    num += 1
            if num > 2:
                tot += 1
    print("solution 1: ", tot)

    op_dict = {}
    op_dict[0] = muli
    op_dict[1] = bani
    while True:
        for num, ops in pot_ops.items():
            if num not in op_dict:
                for _, o in op_dict.items():
                    ops = list(filter(lambda a: a != o, ops))
                freqs = numpy.bincount(ops)
                print(num, freqs)
                top = numpy.argwhere(freqs == numpy.amax(freqs))
                if len(top) == 1:
                    op_dict[num] = operations[top[0][0]]
        if len(op_dict) == len(operations):
            break
        print(op_dict)

    # registers = [0, 0, 0, 0]
    # for line in open("16_program.txt"):
    #     op = re.split('\W+', line)[0:4]
    #     op = [int(o) for o in op]
    #     print(op)
    #     registers = op_dict[op[0]](registers, op[1], op[2], op[3])
    #     print("op: ", op_dict[op[0]])
    #     print("regs: ", registers)
    # print(registers)


if __name__ == "__main__":
    print("Solution")  # 636 too low
    print(solution_1("16.txt"))
