class UnionFind:
    def __init__(self, nodes):
        self.link = {node: None for node in nodes}
        self.size = {node: 1 for node in nodes}

    def find(self, x):
        while self.link[x]:
            x = self.link[x]
        return x

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b: return

        if self.size[a] > self.size[b]:
            a, b = b, a
        self.link[a] = b
        self.size[b] += self.size[a]
        
class WallGrid:
    def __init__(self, n):
        squares = [(x, y) for x in range(1, n + 1) for y in range(1, n + 1)]
        self.uf = UnionFind(squares)
        self.floor = set()
        self.result = 0

    def check(self, pos1, pos2):
        if pos2 in self.floor:
            if self.uf.find(pos1) != self.uf.find(pos2):
                self.result -= 1
                self.uf.union(pos1, pos2)

    def remove(self, x, y):
        if (x, y) in self.floor:
            return
        self.floor.add((x, y))

        self.result += 1

        self.check((x, y), (x - 1, y))
        self.check((x, y), (x + 1, y))
        self.check((x, y), (x, y - 1))
        self.check((x, y), (x, y + 1))

    def count(self):
        return self.result
 
if __name__ == "__main__":
    w = WallGrid(5)
    print(w.count()) # 0
    w.remove(2, 2)
    w.remove(4, 2)
    print(w.count()) # 2
    w.remove(3, 2)
    print(w.count()) # 1
    w.remove(2, 4)
    w.remove(2, 4)
    w.remove(4, 4)
    print(w.count()) # 3
    w.remove(3, 3)
    print(w.count()) # 3
    w.remove(3, 4)
    print(w.count()) # 1