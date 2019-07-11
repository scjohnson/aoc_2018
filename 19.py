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


def solution_1(file_name):
    lines = [line.rstrip() for line in open(file_name)]

    base_reg = int(lines[0].split()[-1])
    ip = 0
    instructions = lines[1:]
    registers = [0, 0, 0, 0, 0, 0]


    while ip < len(instructions):
        ins = instructions[ip].split()
        registers[base_reg] = ip
        registers = eval(ins[0])(registers, int(ins[1]), int(ins[2]), int(ins[3]))
        ip = registers[base_reg] + 1
    return registers[0]
    return


if __name__ == "__main__":
    print(solution_1("19_test.txt"))
    print(solution_1("19.txt")) # 1500
    # print(solution_2("19.txt")) # 1500
