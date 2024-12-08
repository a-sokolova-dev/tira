import heapq

class BestRoute:
    def __init__(self, n):
        self.cities = {}
        for i in range(n):
            self.cities[i+1] = []

    def add_road(self, a, b, x):
        self.cities[a].append((b, x))
        self.cities[b].append((a, x))

    def find_route(self, start, end):
        distances = {}
        for city in self.cities:
            distances[city] = float("inf")
        distances[start] = 0

        queue = []
        heapq.heappush(queue, (0, start))

        visited = set()
        while queue:
            a = heapq.heappop(queue)[1]
            if a in visited:
                continue
            visited.add(a)

            for b, weight in self.cities[a]:
                new_distance = distances[a] + weight
                if new_distance < distances[b]:
                    distances[b] = new_distance
                    new_pair = (new_distance, b)
                    heapq.heappush(queue, new_pair)

        return distances[end] if distances[end] != float("inf") else -1


if __name__ == "__main__":
    b = BestRoute(3)
    b.add_road(1, 2, 2)
    print(b.find_route(1, 3)) # -1
    b.add_road(1, 3, 5)
    print(b.find_route(1, 3)) # 5
    b.add_road(2, 3, 1)
    print(b.find_route(1, 3)) # 3