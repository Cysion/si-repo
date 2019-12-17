import random


class Grid:
    def __init__(self, emp, occ):
        self.grid = []
        self.emp = emp
        self.occ = occ
        self.stats = [1, 1, 1, 1, 1, 1, 1]

    def make(self, xc, yc):
        y = []
        while len(y) != yc:
            x = []
            while len(x) != xc:
                x.append(self.emp)
            y.append(x)
        self.matrix = y

    def print(self):
        live_amount=0
        dead_amount=0
        for y in self.matrix:
            for x in y:
                if x == self.occ:
                    live_amount+=1
                elif x == self.emp:
                    dead_amount+=1
                print(x, end="", flush=True)
            print("")
        print("-" * len(self.matrix[0]))
        print(f"Live cells: {live_amount} | Dead cells: {dead_amount} | Births: {self.stats[0]} | Deaths: {self.stats[1]} | Birth/death ratio: {round(self.stats[0]/self.stats[1], 2)} | Total births: {self.stats[2]} | Total deaths: {self.stats[3]} | Generation: {self.stats[4]} | Generations/sec: {self.stats[5]}")

    def maketest(self, xc, yc):
        i = 0
        y = []
        while len(y) != yc:
            x = []
            while len(x) != xc:
                x.append(f"{i} ")
                i += 1
            y.append(x)
        self.matrix = y

    def rfill(self):
        yc = 0
        for y in self.matrix:
            xc = 0
            for x in y:
                if random.getrandbits(1) == 1:
                    self.matrix[yc][xc] = self.occ
                xc += 1
            yc += 1

    def neighbours(self, x, y, incl):
        neighbours = []
        lenx = len(self.matrix[y]) - 1
        leny = len(self.matrix) - 1

        if (x > 0) and (y > 0):
            neighbours.append(self.matrix[y - 1][x - 1])

        if y > 0:
            neighbours.append(self.matrix[y - 1][x])

        if (y > 0) and (x < lenx):
            neighbours.append(self.matrix[y - 1][x + 1])

        if x > 0:
            neighbours.append(self.matrix[y][x - 1])

        if incl == True:
            neighbours.append(self.matrix[y][x])

        if x < lenx:
            neighbours.append(self.matrix[y][x + 1])

        if (y < leny) and (x > 0):
            neighbours.append(self.matrix[y + 1][x - 1])

        if y < leny:
            neighbours.append(self.matrix[y + 1][x])

        if (y < leny) and (x < lenx):
            neighbours.append(self.matrix[y + 1][x + 1])

        return neighbours