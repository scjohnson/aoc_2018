import matplotlib.pyplot as plt
import numpy


class Point():
    x = 0
    y = 0
    dx = 0
    dy = 0

    def propagate(self, steps):
        for _ in range(steps):
            self.x = self.x + self.dx
            self.y = self.y + self.dy


def solution_1(file_name):
    points = []
    for line in open(file_name):
        line = line.split('>')
        position = line[0].split('<')[1]
        velocity = line[1].split('<')[1]
        point = Point()
        point.x = int(position.split(',')[0])
        point.y = int(position.split(',')[1])
        point.dx = int(velocity.split(',')[0])
        point.dy = int(velocity.split(',')[1])
        points.append(point)

    time = 0
    prev_var = 0
    for p in points:
        p.propagate(10880)

    while True:
        x = []
        y = []
        for point in points:
            x.append(point.x)
            y.append(point.y)
            point.propagate(1)
        
        fig, ax = plt.subplots()
        ax.scatter(x, y,
               alpha=0.3, edgecolors='none')
        plt.show() 
        input(str(time) + ": Press Enter to continue...")
        prev_var = numpy.var(x)

        time += 1
        print(time, prev_var)


if __name__ == "__main__":
    solution_1("10.txt") # ECKXJLJF  after 10880 seconds
