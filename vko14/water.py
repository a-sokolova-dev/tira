"""
CSES-3181 Veden mittaus

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


def count(a, b, x):
    # Very enjoyable task!
    # Got the general idea of how this class of problems might be solved from here:
    # https://blancosilva.github.io/post/2016/07/29/decanting.html

    big = max(a, b)
    small = min(a, b)

    # node format: (big_jug_state, small_jug_state)
    d = construct_graph(big, small)

    distances = d.find_distances((0, 0))
    min_distance = float("inf")

    # remembering which jug was the first one - big or small
    jug_a_idx = 0 if a == big else 1

    for state in distances:
        if (state[jug_a_idx] == x):
            min_distance = min(min_distance, distances[state])

    if min_distance == float("inf"):
        return -1

    return min_distance


def construct_graph(big, small):
    states = [(a, b) for a in range(big + 1) for b in range(small + 1)]
    d = Dijkstra(states)

    # going through all the possible pouring combinations
    for i in range(big + 1):
        for j in range(small + 1):
            # filling empty jugs
            if i == 0:
                d.add_edge((0, j), (big, j), big)
            if j == 0:
                d.add_edge((i, 0), (i, small), small)
            # emptying jugs
            if j != 0:
                d.add_edge((i, j), (i, 0), j)
            if i != 0:
                d.add_edge((i, j), (0, j), i)
            # pouring from a non-empty jug to a non-empty jug
            if i < big and j <= big - i:
                d.add_edge((i, j), (i + j, 0), j)
            if i < big and j > big - i:
                d.add_edge((i, j), (big, j - big + i), big - i)
            if j < small and i <= small - j:
                d.add_edge((i, j), (0, j + i), i)
            if j < small and i > small - j:
                d.add_edge((i, j), (i - small + j, small), small - j)
    return d


if __name__ == "__main__":
    print(count(5, 4, 2))  # 22
    print(count(4, 3, 2))  # 16
    print(count(3, 3, 1))  # -1
    print(count(10, 9, 8))  # 46
    print(count(123, 456, 42))  # 10530
