"""
CSES-3207 Tanssiaiset

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


class Ball:
    def __init__(self, n):
        self.n = n
        self.source_node = 2*n+1
        self.sink_node = 2*n+2
        self.mf = MaximumFlow(range(1, 2*n+3))

        for i in range(1, n+1):
            self.mf.add_edge(self.source_node, i, 1)

        for i in range(1, n+1):
            self.mf.add_edge(i+n, self.sink_node, 1)

    def add_pair(self, a, b):
        self.mf.add_edge(a, b+self.n, 1)

    def calculate(self):
        return self.mf.construct(self.source_node, self.sink_node)


if __name__ == "__main__":
    b = Ball(4)
    print(b.calculate())  # 0
    b.add_pair(1, 2)
    print(b.calculate())  # 1
    b.add_pair(1, 3)
    b.add_pair(3, 2)
    print(b.calculate())  # 2
