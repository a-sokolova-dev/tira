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
    
print("a")

m = MaximumFlow([1, 2, 3, 4, 5, 6, 7])

m.add_edge(1, 2, 7)
m.add_edge(1, 5, 15)

m.add_edge(2, 3, 3)
m.add_edge(2, 4, 2)

m.add_edge(3, 7, 8)

m.add_edge(4, 3, 4)
m.add_edge(4, 7, 3)

m.add_edge(5, 4, 3)
m.add_edge(5, 6, 9)

m.add_edge(6, 4, 5) 
m.add_edge(6, 7, 5) 


print(m.construct(1, 7))