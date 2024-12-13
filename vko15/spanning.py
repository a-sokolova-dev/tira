"""
CSES-3201 Kaikki puut

Please see my GitHub repository for used theory references and writeups:
https://github.com/a-sokolova-dev/tira/tree/main/vko15

Anna Sokolova • December 2024
"""


from itertools import combinations


class AllTrees:
    def __init__(self, n):
        self.nodes = n
        self.edges = []
        self.current_edges = []
        self.visited = set()

    def add_edge(self, a, b):
        self.edges.append((a, b))

    def _is_connected(self, a, b):
        if (a, b) in self.visited:
            return False

        if a == b:
            return True

        self.visited.add((a, b))

        for edge in self.current_edges:
            if edge[0] == a:
                if self._is_connected(edge[1], b):
                    return True

            if edge[1] == a:
                if self._is_connected(edge[0], b):
                    return True

        return False

    def _is_spanning(self, edges):
        # TODO: could be refactored to use UF
        self.current_edges = edges
        for n in range(1, self.nodes+1):
            for m in range(1, self.nodes+1):
                self.visited = set()
                connected = self._is_connected(n, m)
                if not connected:
                    return False

        return True

    def count(self):
        res = 0
        for comb in combinations(self.edges, self.nodes-1):
            if self._is_spanning(comb):
                res += 1

        return res


if __name__ == "__main__":
    a = AllTrees(3)
    a.add_edge(1, 2)
    print(a.count())  # 0
    a.add_edge(1, 3)
    print(a.count())  # 1
    a.add_edge(2, 3)
    print(a.count())  # 3
