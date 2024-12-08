class UnionFind:
    def __init__(self, nodes):
        self.link = {node: None for node in nodes}
        self.size = {node: 1 for node in nodes}

    def find(self, x):
        if self.link[x] is None:
            return x
        self.link[x] = self.find(self.link[x])
        return self.link[x]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a == root_b:
            return

        if self.size[root_a] < self.size[root_b]:
            root_a, root_b = root_b, root_a

        self.link[root_a] = root_b
        self.size[root_b] += self.size[root_a]


class Kruskal:
    def __init__(self, nodes):
        self.nodes = nodes
        self.edges = []

    def add_edge(self, node_a, node_b, weight):
        self.edges.append((node_a, node_b, weight))

    def construct(self):
        self.edges.sort(key=lambda x: x[2])

        uf = UnionFind(self.nodes)
        tree_weight = 0
        edges_count = 0

        for node_a, node_b, weight in self.edges:
            if uf.find(node_a) != uf.find(node_b):
                uf.union(node_a, node_b)
                tree_weight += weight
                edges_count += 1

        return tree_weight if edges_count == len(self.nodes) - 1 else None


class NewRoads:
    def __init__(self, n):
        self.kruskal = Kruskal(range(1, n + 1))

    def add_road(self, a, b, x):
        self.kruskal.add_edge(a, b, x)

    def min_cost(self):
        cost = self.kruskal.construct()
        return cost if cost is not None else -1


if __name__ == "__main__":
    n = NewRoads(4)
    n.add_road(1, 2, 2)
    n.add_road(1, 3, 5)
    print(n.min_cost())  # -1
    n.add_road(3, 4, 4)
    print(n.min_cost())  # 11
    n.add_road(2, 3, 1)
    print(n.min_cost())  # 7
