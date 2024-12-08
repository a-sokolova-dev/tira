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
    n = len(r)
    nodes = [(y, x, k) for y in range(n) for x in range(n) for k in [0, 1]]

    mf = MaximumFlow(nodes)

    for y in range(n):
        for x in range(n):
            if r[y][x] == ".":
                mf.add_edge((y, x, 0), (y, x, 1), 1)

            if y + 1 < n:
                mf.add_edge((y, x, 1), (y + 1, x, 0), 1)

            if x + 1 < n:
                mf.add_edge((y, x, 1), (y, x + 1, 0), 1)

    return mf.construct((0, 0, 1), (n - 1, n - 1, 0))

if __name__ == "__main__":
    r = [".....",
         ".###.",
         "...#.",
         "##.#.",
         "....."]
    print(count(r)) # 2

    r = [".....",
         ".....",
         "..#.#",
         ".....",
         "..#.."]
    print(count(r)) # 1