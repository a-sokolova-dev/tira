from collections import deque
import time

n = 10**5

# lisäysaika
start_time = time.time()
d = deque()
for i in range(1, n+1):
    d.append(i)
append_time = time.time() - start_time

# poistoaika
start_time = time.time()
for _ in range(n):
    d.popleft()
remove_time = time.time() - start_time

print(f"Lisäämisen kesto: {append_time:.6f} sekuntia")
print(f"Poistamisen kesto: {remove_time:.6f} sekuntia")