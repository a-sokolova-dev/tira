"""
CSES-3179 Listahyppy

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

    def find_distances(self, start_node):
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

        return distances


def calculate(t):
    # refactored to use Dijkstra's
    n = len(t)
    d = Dijkstra(range(n))

    for i in range(n):
        if i - t[i] >= 0:
            d.add_edge(i, i - t[i], t[i])
        if i + t[i] < n:
            d.add_edge(i, i + t[i], t[i])

    from_node = 0
    to_node = n - 1
    distances = d.find_distances(from_node)

    return distances[to_node] if distances[to_node] != float('inf') else -1


if __name__ == "__main__":
    print(calculate([1, 1, 1, 1]))  # 3
    print(calculate([3, 2, 1]))      # -1
    print(calculate([3, 5, 2, 2, 2, 3, 5]))  # 10
    print(calculate([7, 5, 3, 1, 4, 2, 4, 6, 1]))  # 32
