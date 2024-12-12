"""
CSES-3180 Seinäpoisto

Please see my GitHub repository for used theory references and writeups:
https://github.com/a-sokolova-dev/tira/tree/main/vko14

Anna Sokolova • December 2024
"""


import heapq


class Dijkstra:
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = {node: [] for node in nodes}

    def add_edge(self, node_a, node_b, weight):
        self.graph[node_a].append((node_b, weight))

    def find_distance(self, start_node, end_node):
        distances = {}
        for node in self.nodes:
            distances[node] = float("inf")
        distances[start_node] = 0

        queue = []
        heapq.heappush(queue, (0, start_node))

        visited = set()
        while queue:
            node_a = heapq.heappop(queue)[1]
            if node_a in visited:
                continue
            visited.add(node_a)

            for node_b, weight in self.graph[node_a]:
                new_distance = distances[node_a] + weight
                if new_distance < distances[node_b]:
                    distances[node_b] = new_distance
                    new_pair = (new_distance, node_b)
                    heapq.heappush(queue, new_pair)

        return distances[end_node]


def count(r):
    # could be solved using Bellman-Ford's algorithm
    # but I really like Dijkstra's...
    rows = len(r)
    columns = len(r[0])
    d = Dijkstra(range(len(r) * len(r[0])))
    
    for i, row in enumerate(r):
        for j, tile in enumerate(row):
            if tile == "A":
                A = i * columns + j
            if tile == "B":
                B = i * columns + j
            for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= ni < rows and 0 <= nj < columns:
                    w = 0
                    if r[ni][nj] == "*":
                        w = 1
                    elif r[ni][nj] == "#":
                        continue
                    d.add_edge(i * columns + j, ni * columns + nj, w)

    return d.find_distance(A, B)


if __name__ == "__main__":
    r = ["########",
         "#*A*...#",
         "#.*****#",
         "#.**.**#",
         "#.*****#",
         "#..*.B.#",
         "########"]
    print(count(r))  # 2
