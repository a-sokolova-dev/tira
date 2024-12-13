"""
CSES-3209 Uudet seinät

Please see my GitHub repository for used theory references and writeups:
https://github.com/a-sokolova-dev/tira/tree/main/vko16

Anna Sokolova • December 2024
"""


class MaximumFlow:
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = {}
        for i in self.nodes:
            for j in self.nodes:
                self.graph[(i, j)] = 0

    def add_edge(self, node_a, node_b, capacity):
        self.graph[(node_a, node_b)] += capacity

    def add_flow(self, node, sink, flow):
        if node in self.seen:
            return 0
        self.seen.add(node)
        if node == sink:
            return flow
        for next_node in self.nodes:
            if self.flow[(node, next_node)] > 0:
                new_flow = min(flow, self.flow[(node, next_node)])
                inc = self.add_flow(next_node, sink, new_flow)
                if inc > 0:
                    self.flow[(node, next_node)] -= inc
                    self.flow[(next_node, node)] += inc
                    return inc
        return 0

    def construct(self, source, sink):
        self.flow = self.graph.copy()
        total = 0
        while True:
            self.seen = set()
            add = self.add_flow(source, sink, float("inf"))
            if add == 0:
                break
            total += add
        return total


def count(r):
    # had too much fun trying to refactor this, so
    # that's why the multiple re-submissions. sorry.
    size = len(r) * len(r) * 2
    mf = MaximumFlow(range(0, size))

    for x in range(len(r)):
         for y in range(len(r)):
            if r[x][y] == "#":
                continue

            node_base = (x * len(r) + y) * 2
            mf.add_edge(node_base, node_base + 1, 1)

            if x < len(r) - 1:
                mf.add_edge(node_base + 1, ((x + 1) * len(r) + y) * 2, 1)

            if y < len(r) - 1:
                mf.add_edge(node_base + 1, (x * len(r) + (y + 1)) * 2, 1)

    return mf.construct(1, size - 2)


if __name__ == "__main__":
    r = [".....",
         ".###.",
         "...#.",
         "##.#.",
         "....."]
    print(count(r))  # 2

    r = [".....",
         ".....",
         "..#.#",
         ".....",
         "..#.."]
    print(count(r))  # 1
