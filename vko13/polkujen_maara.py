class CountPaths:
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = {node: [] for node in self.nodes}

    def add_edge(self, a, b):
        self.graph[a].append(b)

    def count_from(self, node):
        if node in self.result:
            return self.result[node]

        path_count = 0
        for next_node in self.graph[node]:
            path_count += self.count_from(next_node)

        self.result[node] = path_count
        return path_count

    def count_paths(self, x, y):
        self.result = {y: 1}
        return self.count_from(x)
    
def create_graph():
    nodes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    
    G = CountPaths(nodes)
    
    edges = [
        (0, 1), (0, 2), (0, 3), (0, 4), (0, 5),
        
        (1, 6), (1, 7), (1, 8), (1, 9), (1, 10),
        (2, 6), (2, 7), (2, 8), (2, 9), (2, 10),
        (3, 6), (3, 7), (3, 8), (3, 9), (3, 10),
        (4, 6), (4, 7), (4, 8), (4, 9), (4, 10),
        (5, 6), (5, 7), (5, 8), (5, 9), (5, 10),
        
        (6, 11), (6, 12), (6, 13), (6, 14),
        (7, 11), (7, 12), (7, 13), (7, 14),
        (8, 11), (8, 12), (8, 13), (8, 14),
        (9, 11), (9, 12), (9, 13), (9, 14),
        (10, 11), (10, 12), (10, 13), (10, 14),
        
        (11, 15), (12, 15), (13, 15), (14, 15)
    ]
    
    for a, b in edges:
        G.add_edge(a, b)
    
    return G

graph = create_graph()
paths = graph.count_paths(0, 15)

print(f"Polkujen määrä: {paths}")
assert paths == 100, f"Virhe: Polkuja on {paths}, mutta pitäisi olla 100"