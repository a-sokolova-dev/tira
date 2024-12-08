from heapq import heappush, heappop

class Median:
    def __init__(self):
        self.right = []
        self.left = []

     # left heap stores numbers as negatives
     # since heapq is minheap and we median to be on top
     
    def add(self, x):
        if not self.left:
            heappush(self.left, -x)
            return

        if x < -self.left[0]:
            heappush(self.left, -x)
        else:
            heappush(self.right, x)


        if len(self.left) > len(self.right) + 1:
            heappush(self.right, -heappop(self.left))
        elif len(self.right) > len(self.left):
            heappush(self.left, -heappop(self.right))


    def median(self):
        return -self.left[0]
    
if __name__ == "__main__":
    m = Median()
    m.add(1)
    print(m.median()) # 1
    m.add(2)
    print(m.median()) # 1
    m.add(1)
    print(m.median()) # 1
    m.add(3)
    print(m.median()) # 1
    m.add(3)
    print(m.median()) # 2
    