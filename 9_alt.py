# Solve problem nine
import numpy
import tqdm

class LinkedList()

def solution_1(players, last_marble):
    marble_list = []
    scores = numpy.zeros(players)

    marble_list = numpy.zeros(last_marble)
    marble_list[0] = 0
    marble_list[1] = 1
    max_index = 2

    # marble_list = numpy.array([0, 1])
    index = 1
    player = 1
    for i in tqdm.tqdm(range(2, last_marble + 1)):
        if i % 23 == 0:
            scores[player] += i
            index -= 9
            # index = index % len(marble_list)
            index = index % max_index
            scores[player] += marble_list[index]
            # marble_list = marble_list[0:index] + marble_list[index+1:]
            # marble_list = numpy.delete(marble_list, index)
            # marble_list[index:max_index] = marble_list[index+1:max_index+1]
            numpy.copyto(marble_list[index:max_index], marble_list[index+1:max_index+1])
            max_index -= 1
        else:
            # marble_list = marble_list[0:index] + [i] + marble_list[index:]
            # marble_list = numpy.insert(marble_list, index, i)
            # marble_list[index+1:max_index+1] = marble_list[index:max_index]
            numpy.copyto(marble_list[index+1:max_index+1], marble_list[index:max_index])
            marble_list[index] = i
            max_index += 1

        player += 1
        player = player % players
        index += 2
        # index = index % len(marble_list)
        index = index % max_index
    return max(scores)


if __name__ == "__main__":
    print("Solution 1 test: ", solution_1(9, 25), " =? 32")
    print("Solution 1 test: ", solution_1(10, 1618), " =? 8317")
    print("Solution 1 test: ", solution_1(13, 7999), " =? 146373")
    print("Solution 1 test: ", solution_1(17, 1104), " =? 2764")
    print("Solution 1 test: ", solution_1(21, 6111), " =? 54718")
    print("Solution 1: ", solution_1(459, 72103))  # 388131
    print("Solution 2: ", solution_1(459, 7210300))
