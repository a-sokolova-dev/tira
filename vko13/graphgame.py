class GraphGame:
    def __init__(self, n):
        self.nodes = {node: [] for node in range(1, n+1)}
        self.cache = {}

    def add_link(self, a, b):
        self.nodes[a].append(b)
        self.cache = {}

    def winning(self, x):
        if x in self.cache:
            return self.cache[x]

        for node in self.nodes[x]:
            if not self.winning(node):
                self.cache[x] = True
                return True
        
        self.cache[x] = False
        return False

if __name__ == "__main__":
    g = GraphGame(6)
    g.add_link(3, 4)
    g.add_link(1, 4)
    g.add_link(4, 5)
    print(g.winning(3)) # False
    print(g.winning(1)) # False
    g.add_link(3, 1)
    g.add_link(4, 6)
    g.add_link(6, 5)
    print(g.winning(3)) # True
    print(g.winning(1)) # False
    print(g.winning(2)) # False