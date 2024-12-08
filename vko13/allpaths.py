class AllPaths:
    def __init__(self, n):
        self.nodes = {}
        for i in range(n):
            self.nodes[i+1] = []
        self.cache = {}

    def add_edge(self, a, b):
        self.nodes[a].append(b)
        self.cache = {}
        
    def count_helper(self, node):
        if node in self.cache:
            return self.cache[node]

        count = 0
        for dest in self.nodes[node]:
            count += self.count_helper(dest) + 1

        self.cache[node] = count
        return count

    def count(self):
        count = 0
        for node in self.nodes:
            count += self.count_helper(node) + 1

        return count
        

if __name__ == "__main__":
    a = AllPaths(4)
    a.add_edge(1, 2)
    a.add_edge(1, 3)
    a.add_edge(2, 4)
    a.add_edge(3, 4)
    print(a.count()) # 10
    a.add_edge(2, 3)
    print(a.count()) # 14