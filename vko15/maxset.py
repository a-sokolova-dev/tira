class UnionFind:
    def __init__(self, nodes):
        self.link = {node: None for node in nodes}
        self.size = {node: 1 for node in nodes}
        self.max = 1
 
    def find(self, x):
        while self.link[x]:
            x = self.link[x]
        return x
 
    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b: return
 
        if self.size[a] > self.size[b]:
            a, b = b, a
        self.link[a] = b
        self.size[b] += self.size[a]

        self.max = max(self.max, self.size[b])
        
 
class MaxSet:
    def __init__(self, n):
        self.n = n
        self.uf = UnionFind(range(1, n+1))
 
    def merge(self, a, b):
        self.uf.union(a, b)
 
    def get_max(self):
        return self.uf.max
 
if __name__ == "__main__":
    m = MaxSet(5)
    print(m.get_max()) # 1
    m.merge(1, 2)
    m.merge(3, 4)
    m.merge(3, 5)
    print(m.get_max()) # 3
    m.merge(1, 5)
    print(m.get_max()) # 5
