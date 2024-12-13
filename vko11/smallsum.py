# confusing task description, will attempt it again later
import heapq

class Heap:
    def __init__(self, n):
        self.v = [0] * n
        self.n = n
        
def left(i):
    return 2 * i + 1

def right(i):
    return 2 * i + 2


def find(n):
    h = Heap(n)
    h.v = list(range(n))

    return findKthSmallest(h, n)

def findKthSmallest(h, k):
    p = []
 
    heapq.heappush(p, (h.v[0], 0))
 
    for i in range(k - 1):
        j = heapq.heappop(p)[1]
        l, r = left(j), right(j)
        if l < h.n:
            heapq.heappush(p, (h.v[l], l))
        if r < h.n:
            heapq.heappush(p, (h.v[r], r))
 
    return p[0][0]

if __name__ == "__main__":
    print(find(1)) # 0
    print(find(2)) # 1
    print(find(3)) # 2
    print(find(4)) # 3
    print(find(5)) # 3
    print(find(123)) # 15
    print(find(123456)) # 62