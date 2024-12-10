"""
CSES-3142 Listan pienin

Please see my GitHub repository for used theory references and writeups:
https://github.com/a-sokolova-dev/tira/tree/main/vko11

Anna Sokolova • December 2024
"""


import heapq


def smallest(n):
    keko = []
    heapq.heappush(keko, 1)

    for _ in range(n):
        pienin = heapq.heappop(keko)
        heapq.heappush(keko, pienin * 2)
        heapq.heappush(keko, pienin * 3)

    return heapq.heappop(keko)


if __name__ == "__main__":
    print(smallest(1))  # 2
    print(smallest(5))  # 6
    print(smallest(123))  # 288
    print(smallest(55555))  # 663552
