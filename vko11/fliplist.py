"""
CSES-3143 Kääntölista

Please see my GitHub repository for used theory references and writeups:
https://github.com/a-sokolova-dev/tira/tree/main/vko11

Anna Sokolova • December 2024
"""


import collections


class FlipList:
    def __init__(self):
        self.deque = collections.deque()
        self.flipped = False

    def push_first(self, x):
        if not self.flipped:
            return self.deque.appendleft(x)

        return self.deque.append(x)

    def push_last(self, x):
        if not self.flipped:
            return self.deque.append(x)

        return self.deque.appendleft(x)

    def pop_first(self):
        if not self.flipped:
            return self.deque.popleft()

        return self.deque.pop()

    def pop_last(self):
        if not self.flipped:
            return self.deque.pop()

        return self.deque.popleft()

    def flip(self):
        self.flipped = not self.flipped


if __name__ == "__main__":
    f = FlipList()
    f.push_last(1)
    f.push_last(2)
    f.push_last(3)
    print(f.pop_first())  # 1
    f.flip()
    print(f.pop_first())  # 3
