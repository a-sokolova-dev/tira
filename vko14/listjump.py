import heapq

def calculate(t):
    n = len(t)
    
    graph = {i: [] for i in range(n)}
    for i, v in enumerate(t):
        if i - v >= 0:
            graph[i].append((i - v, v))
        if i + v < n:
            graph[i].append((i + v, v))
    
    distances = {i: float('inf') for i in range(n)}
    distances[0] = 0
    
    queue = [(0, 0)]
    heapq.heapify(queue)
    
    visited = set()
    
    while queue:
        current_distance, node_a = heapq.heappop(queue)
        
        if node_a in visited:
            continue
        visited.add(node_a)

        for node_b, weight in graph[node_a]:
            new_distance = current_distance + weight
            if new_distance < distances[node_b]:
                distances[node_b] = new_distance
                heapq.heappush(queue, (new_distance, node_b))

    return distances[n - 1] if distances[n - 1] != float('inf') else -1

if __name__ == "__main__":
    print(calculate([1, 1, 1, 1]))  # 3
    print(calculate([3, 2, 1]))      # -1
    print(calculate([3, 5, 2, 2, 2, 3, 5]))  # 10
    print(calculate([7, 5, 3, 1, 4, 2, 4, 6, 1]))  # 32
