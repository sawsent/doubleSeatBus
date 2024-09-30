class Bus:
    def __init__(self, BUS_SEATS) -> None:
        self.seats = BUS_SEATS
        self.repr = [0 for x in range(int(BUS_SEATS/2))]

    def join(self, agressiveness):
        idx = self.leastAgressive()
        if self.repr[idx] == 0:
            self.repr[idx] = agressiveness
        else:
            self.repr[idx] = 1
        return idx

    def leastAgressive(self):
        min = 1
        idx = 0
        for i, x in enumerate(self.repr):
            if x == 0:
                return i
            if x < min:
                min = x
                idx = i
        return idx

    def isAlone(self, i):
        return self.repr[i] != 1

    def print(self):
        map = {i + 1: a for i, a in enumerate(self.repr)}

        print(map)
