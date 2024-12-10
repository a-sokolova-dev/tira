"""
CSES-3146 Mediaani

Please see my GitHub repository for used theory references and writeups:
https://github.com/a-sokolova-dev/tira/tree/main/vko11

Anna Sokolova • December 2024
"""


import heapq


class Median:
    def __init__(self):
        self.right = []
        self.left = []

     # left heap stores numbers as negatives
     # since heapq is minheap and we median to be on top

    def add(self, x):
        if not self.left:
            heapq.heappush(self.left, -x)
            return

        if x < -self.left[0]:
            heapq.heappush(self.left, -x)
        else:
            heapq.heappush(self.right, x)

        if len(self.left) > len(self.right) + 1:
            heapq.heappush(self.right, -heapq.heappop(self.left))
        elif len(self.right) > len(self.left):
            heapq.heappush(self.left, -heapq.heappop(self.right))

    def median(self):
        return -self.left[0]


if __name__ == "__main__":
    m = Median()
    m.add(1)
    print(m.median())  # 1
    m.add(2)
    print(m.median())  # 1
    m.add(1)
    print(m.median())  # 1
    m.add(3)
    print(m.median())  # 1
    m.add(3)
    print(m.median())  # 2
