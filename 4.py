import numpy


def get_guards(file_name):
    guard = -1
    asleep = False
    asleep_minute = -1
    guards = {}
    for line in open(file_name):
        if '#' in line:
            guard = int(line.split('#')[1].split(' ')[0])
            asleep = False
            if guard not in guards:
                guards[guard] = numpy.zeros((60))
        else:
            minute = int(line.split(']')[0].split(':')[1])
            if asleep:
                if "wakes up" in line:
                    guards[guard][asleep_minute:minute] += 1
                    asleep = False
            elif "falls asleep" in line:
                asleep_minute = minute
                asleep = True
    return guards


def solution_1(guards):
    most_minutes = 0
    max_guard = 0
    max_minute = 0
    for g, mins in guards.items():
        if numpy.sum(mins) > most_minutes:
            max_guard = g
            max_minute = numpy.argmax(mins)
            most_minutes = numpy.sum(mins)
    return (max_guard, max_minute, max_guard*max_minute)

def solution_2(guards):
    max_guard = 0
    max_value = 0
    max_minute = -1
    for g, mins in guards.items():
        if numpy.max(mins) > max_value:
            max_guard = g
            max_value = numpy.max(mins)
            max_minute = numpy.argmax(mins)
    return (max_guard, max_minute, max_guard*max_minute)

if __name__ == "__main__":
    guards = get_guards("4.txt")
    print("Solution 1: ", solution_1(guards)) #72925
    print("Solution 2: ", solution_2(guards)) #49137
