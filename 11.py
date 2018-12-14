import numpy
from itertools import product

def solution_1(file_name):
    serial_number = 6303
    powers = numpy.zeros([300, 300])
    for i, j in product(range(300), range(300)):
        rack_id = i+10
        power_level = rack_id*j
        power_level += serial_number
        power_level *= rack_id
        if power_level < 100:
            power_level = 0
        else:
            power_level = int(str(power_level)[-3])
        power_level -= 5
        powers[i, j] = power_level

    max_value = 0
    max_i = 0
    max_j = 0
    for i, j in product(range(298), range(298)):
        power = numpy.sum(powers[i:i+3,j:j+3])
        if power > max_value:
            max_i = i
            max_j = j
            max_value = power
    print (max_i, max_j, max_value)

    max_value = 0
    max_i = 0
    max_j = 0
    max_k = 0
    for k in range(300):
        for i, j in product(range(300-k), range(300-k)):
            power = numpy.sum(powers[i:i+k,j:j+k])
            if power > max_value:
                max_i = i
                max_j = j
                max_k = k
                max_value = power
    print (max_i, max_j, max_k, max_value) # 284,172,88
    return

    


if __name__ == "__main__":
    print(solution_1("10.txt")) # 284,172,88
