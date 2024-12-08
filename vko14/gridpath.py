import heapq

class Dijkstra:
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = {node: [] for node in nodes}

    def add_edge(self, node_a, node_b, weight):
        self.graph[node_a].append((node_b, weight))

    def find_distance(self, start_node, end_node):
        distances = {node: float("inf") for node in self.nodes}
        distances[start_node] = 0

        queue = [(0, start_node)]
        visited = set()

        while queue:
            current_distance, node_a = heapq.heappop(queue)

            if node_a in visited:
                continue
            visited.add(node_a)

            for node_b, weight in self.graph[node_a]:
                new_distance = current_distance + weight
                if new_distance < distances[node_b]:
                    distances[node_b] = new_distance
                    heapq.heappush(queue, (new_distance, node_b))

        return distances[end_node]


def count(r):
    rows = len(r)
    cols = len(r[0])

    dijkstra = Dijkstra(range(rows * cols))

    for i in range(rows):
        for j in range(cols):
            node_a = i * cols + j
            for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= ni < rows and 0 <= nj < cols:
                    node_b = ni * cols + nj
                    dijkstra.add_edge(node_a, node_b, r[ni][nj])

    end_node = (rows - 1) * cols + (cols - 1)
    return dijkstra.find_distance(0, end_node) + r[0][0]


if __name__ == "__main__":
    r = [[2, 1, 4, 8],
         [3, 8, 7, 2],
         [9, 5, 1, 2]]
    print(count(r))  # Output: 17
