import numpy
from collections import Counter
from difflib import SequenceMatcher
from itertools import combinations

def solution_1(file_name):
    maxx = 1000
    maxy = 1000
    claims = numpy.zeros(shape=(maxx, maxy))
    for line in open(file_name):
        elems = line.split(' ')
        claim = elems[0]
        location = elems[2][0:-1]
        location = location.split(',')
        location = (int(location[0]), int(location[1]))
        shape = elems[3]
        shape = shape.split('x')
        shape = (int(shape[0]), int(shape[1]))
        claims[location[0]:location[0]+shape[0], location[1]:location[1]+shape[1]] += 1
    return numpy.sum(claims>1)

def solution_2(file_name):
    maxx = 1000
    maxy = 1000
    claims = numpy.zeros(shape=(maxx, maxy))
    for line in open(file_name):
        elems = line.split(' ')
        claim = elems[0]
        location = elems[2][0:-1]
        location = location.split(',')
        location = (int(location[0]), int(location[1]))
        shape = elems[3]
        shape = shape.split('x')
        shape = (int(shape[0]), int(shape[1]))
        claims[location[0]:location[0]+shape[0], location[1]:location[1]+shape[1]] += 1
    for line in open(file_name):
        elems = line.split(' ')
        claim = elems[0]
        location = elems[2][0:-1]
        location = location.split(',')
        location = (int(location[0]), int(location[1]))
        shape = elems[3]
        shape = shape.split('x')
        shape = (int(shape[0]), int(shape[1]))
        trues = (claims[location[0]:location[0]+shape[0], location[1]:location[1]+shape[1]] == 1)
        if trues.all():
            print(claims[location[0]:location[0]+shape[0], location[1]:location[1]+shape[1]])
            return claim
    return False


if __name__ == "__main__":
    print("Solution 1: ", solution_1("3.txt")) #
    print("Solution 2: ", solution_2("3.txt")) #
