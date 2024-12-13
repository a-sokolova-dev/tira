"""
CSES-3200 Seinät ja lattiat

Please see my GitHub repository for used theory references and writeups:
https://github.com/a-sokolova-dev/tira/tree/main/vko15

Anna Sokolova • December 2024
"""


class UnionFindTuple:
    def __init__(self, tuples):
        self.link = {(x, y): None for x in tuples for y in tuples}
        self.size = {(x, y): 0 for x in tuples for y in tuples}

    def find(self, x):
        while self.link[x]:
            x = self.link[x]
        return x

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return

        if self.size[a] > self.size[b]:
            a, b = b, a
        self.link[a] = b
        self.size[b] += self.size[a]


class WallGrid:
    def __init__(self, n):
        self.uf = UnionFindTuple(range(1, n+1))
        self.rooms = 0

    def remove(self, x, y):
        if self.uf.size[(x, y)]:
            return

        self.uf.size[(x, y)] += 1
        self.rooms += 1

        adjacent = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

        for cell in adjacent:
            if self.uf.size.get(cell, 0):
                if self.uf.find(cell) != self.uf.find((x, y)):
                    self.uf.union((x, y), cell)
                    self.rooms -= 1

    def count(self):
        return self.rooms


if __name__ == "__main__":
    w = WallGrid(5)
    print(w.count())  # 0
    w.remove(2, 2)
    w.remove(4, 2)
    print(w.count())  # 2
    w.remove(3, 2)
    print(w.count())  # 1
    w.remove(2, 4)
    w.remove(2, 4)
    w.remove(4, 4)
    print(w.count())  # 3
    w.remove(3, 3)
    print(w.count())  # 3
    w.remove(3, 4)
