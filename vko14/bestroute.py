"""
CSES-3178 Paras reitti

Please see my GitHub repository for used theory references and writeups:
https://github.com/a-sokolova-dev/tira/tree/main/vko14

Anna Sokolova • December 2024
"""


import heapq


class BellmanFord:
    def __init__(self, nodes):
        self.nodes = nodes
        self.edges = []

    def add_edge(self, node_a, node_b, weight):
        self.edges.append((node_a, node_b, weight))

    def find_distances(self, start_node):
        distances = {}
        for node in self.nodes:
            distances[node] = float("inf")
        distances[start_node] = 0

        num_rounds = len(self.nodes) - 1
        for _ in range(num_rounds):
            for edge in self.edges:
                node_a, node_b, weight = edge
                new_distance = distances[node_a] + weight
                if new_distance < distances[node_b]:
                    distances[node_b] = new_distance

        return distances


class BestRoute:
    # refactored to use BellFord instead of a more literal approach
    def __init__(self, n):
        self.cities = BellmanFord(range(1, n + 1))

    def add_road(self, a, b, length):
        # adding "twice" since roads are (usually) bidirectional
        self.cities.add_edge(a, b, length)
        self.cities.add_edge(b, a, length)

    def find_route(self, start, end):
        distances = self.cities.find_distances(start)
        distances[start] = 0

        return distances[end] if distances[end] != float("inf") else -1


if __name__ == "__main__":
    b = BestRoute(3)
    b.add_road(1, 2, 2)
    print(b.find_route(1, 3))  # -1
    b.add_road(1, 3, 5)
    print(b.find_route(1, 3))  # 5
    b.add_road(2, 3, 1)
    print(b.find_route(1, 3))  # 3
