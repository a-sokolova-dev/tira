import random
import heapq
import time

# Vakiot
n = 10**6
k = n // 10


random.seed(1337)
data = [random.randint(1, 10**9) for _ in range(n)]

# algoritmi 1: järjestäminen
start_time = time.time()
sorted_data = sorted(data)
sum1 = sum(sorted_data[:k])
time1 = time.time() - start_time

# algoritmi 2: keko
heap = data.copy()

start_time = time.time()
heapq.heapify(heap)
sum2 = sum(heapq.heappop(heap) for _ in range(k))
time2 = time.time() - start_time

print(f"Algoritmi 1: järjestäminen")
print(f"  Algoritmi 1:n kesto: {time1:.6f} sekuntia")
print(f"  Summa: {sum1}")

print(f"\nAlgoritmi 2: keko:")
print(f"  Algoritmi 2:n kesto: {time2:.6f} sekuntia")
print(f"  Summa: {sum2}")