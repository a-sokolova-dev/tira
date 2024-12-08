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
    lenr = len(r)
    lenr0 = len(r[0])
    dijkstra = Dijkstra(range(len(r)*len(r[0])))
    for i, row in enumerate(r):
        for j, tile in enumerate(row):
            if tile == "A":
                A = i*lenr0 + j
            if tile == "B":
                B = i*lenr0 + j
            for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= ni < lenr and 0 <= nj < lenr0:
                    w = 0
                    if r[ni][nj] == "*":
                        w = 1
                    elif r[ni][nj] == "#":
                        continue
                    dijkstra.add_edge(i*lenr0 + j, ni*lenr0 + nj, w)

    return dijkstra.find_distance(A, B)

if __name__ == "__main__":
    r = ["########",
         "#*A*...#",
         "#.*****#",
         "#.**.**#",
         "#.*****#",
         "#..*.B.#",
         "########"]
    print(count(r)) # 2