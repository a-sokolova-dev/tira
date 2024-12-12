import random
import time
import heapq

class Dijkstra:
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = {node: [] for node in nodes}

    def add_edge(self, node_a, node_b, weight):
        self.graph[node_a].append((node_b, weight))

    # added shuffling edges for testing 
    def shuffle_edges(self):
        for node in self.graph:
            random.shuffle(self.graph[node])
            
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
    
def generate_graph(N):
    nodes = list(range(1, N+1))
    graph = Dijkstra(nodes)
    
    for a in range(1, N):
        for b in range(a + 1, min(a + 10, N + 1)):
            weight = random.randint(1, 1000)
            graph.add_edge(a, b, weight)
    
    graph.shuffle_edges()
    return graph

if __name__ == "__main__":
    N = 5000
    
    graph = generate_graph(N)
    start_time = time.time()
    distances = graph.find_distances(1)
    end_time = time.time()
    
    t = end_time - start_time
    print(f"Aika: {t:.6f}")