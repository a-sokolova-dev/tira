import itertools

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
        
class AllTrees:
    def __init__(self, n):
        self.n = n
        self.edges = []

    def add_edge(self, a, b):
        self.edges.append((a, b))

    def is_tree(self, choice):
        uf = UnionFind(range(1, self.n + 1))

        for a, b in choice:
            if uf.find(a) == uf.find(b):
                return False
            uf.union(a, b)

        return True

    def count(self):
        result = 0
        choices = itertools.combinations(self.edges, self.n - 1)

        for choice in choices:
            if self.is_tree(choice):
                result += 1

        return result