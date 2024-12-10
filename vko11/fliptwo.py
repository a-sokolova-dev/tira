"""
CSES-3145 Muuttuva lista

Please see my GitHub repository for used theory references and writeups:
https://github.com/a-sokolova-dev/tira/tree/main/vko11

Anna Sokolova • December 2024
"""

import collections


def solve(n, k):
    queue = collections.deque(range(1, n+1))

    for _ in range(k):
        el1 = queue.popleft()
        el2 = queue.popleft()

        queue.append(el2)
        queue.append(el1)

    return queue.popleft()


if __name__ == "__main__":
    print(solve(4, 3))  # 4
    print(solve(12, 5))  # 11
    print(solve(99, 555))  # 11
    print(solve(12345, 54321))  # 9875
