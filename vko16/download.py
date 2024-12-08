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
    
class Download:
    def __init__(self, n):
        self.mf = MaximumFlow(range(1, n + 1))
 
    def add_link(self, a, b, x):
        self.mf.add_edge(a, b, x)
 
    def calculate(self, a, b):
        return self.mf.construct(a, b)

if __name__ == "__main__":
    d = Download(4)
    print(d.calculate(1, 4)) # 0
    d.add_link(1, 2, 5)
    d.add_link(2, 4, 6)
    d.add_link(1, 4, 2)
    print(d.calculate(1, 4)) # 7
    d.add_link(1, 3, 4)
    d.add_link(3, 2, 2)
    print(d.calculate(1, 4)) # 8