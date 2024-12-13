"""
CSES-3208 Ratsuparit

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
    positions = [(x, y) for x in range(len(r)) for y in range(len(r[0]))]
    mf = MaximumFlow(positions + ["start", "end"])

    knights = [(x, y) for x in range(len(r))
               for y in range(len(r[0])) if r[x][y] == "*"]

    for x, y in knights:
        if (x + y) % 2 == 0:
            mf.add_edge("start", (x, y), 1)
        else:
            mf.add_edge((x, y), "end", 1)

    offsets = [
        (-2, 1), (-2, -1), (2, 1), (2, -1),
        (1, -2), (1, 2), (-1, 2), (-1, -2)
    ]

    for x1, y1 in knights:
        if (x1 + y1) % 2 == 0:
            for dx, dy in offsets:
                x2, y2 = x1 + dx, y1 + dy

                if (0 <= x2 < len(r) and 0 <= y2 < len(r[0]) and
                        r[x2][y2] == "*" and (x2, y2) in knights):
                    mf.add_edge((x1, y1), (x2, y2), 1)

    return mf.construct("start", "end")


if __name__ == "__main__":
    r = ["*.......",
         "..*...*.",
         "........",
         ".*......",
         "...*....",
         ".......*",
         "........",
         "......*."]
    print(count(r))  # 3

    r = ["***.*...",
         ".*...***",
         "**..*..*",
         "..*.*..*",
         ".*.....*",
         ".***.**.",
         "...*...*",
         "**..*.**"]
    print(count(r))  # 10
