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

class Kruskal:
    def __init__(self, nodes):
        self.nodes = nodes
        self.edges = []

    def add_edge(self, node_a, node_b, weight):
        self.edges.append((node_a, node_b, weight))

    def construct(self):
        self.edges.sort(key=lambda x: x[2])

        uf = UnionFind(self.nodes)
        edges_count = 0
        tree_weight = 0

        for edge in self.edges:
            node_a, node_b, weight = edge
            if uf.find(node_a) != uf.find(node_b):
                uf.union(node_a, node_b)
                edges_count += 1
                tree_weight += weight

        if edges_count != len(self.nodes) - 1:
            return None
        return tree_weight


class SameWeight:
    def __init__(self, n):
        self.pos = Kruskal(range(1, n+1))
        self.neg = Kruskal(range(1, n+1))

    def add_edge(self, a, b, x):
        self.pos.add_edge(a, b, x)
        self.neg.add_edge(a, b, -x)

    def check(self):
        pos = self.pos.construct()
        neg = self.neg.construct()
        if pos is None:
            return True
        return pos == -neg

if __name__ == "__main__":
    s = SameWeight(4)
    s.add_edge(1, 2, 2)
    s.add_edge(1, 3, 3)
    print(s.check()) # True
    s.add_edge(1, 4, 3)
    print(s.check()) # True
    s.add_edge(3, 4, 3)
    print(s.check()) # True
    s.add_edge(2, 4, 1)
    print(s.check()) # False