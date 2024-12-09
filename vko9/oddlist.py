"""
CSES-3119 Oudot listat

Please see my GitHub repository for used theory references and writeups:
https://github.com/a-sokolova-dev/tira/tree/main/vko9

Anna Sokolova • December 2024
"""


import itertools


def count(n, x):
    count = 0
    l = list(range(1, n + 1))
    for order in itertools.permutations(l):
        if valid(order, x):
            count += 1
    return count


def valid(permutation, x):
    if permutation[0] != x:
        return False

    unique_sums = set()

    for i in range(0, len(permutation) - 1):
        s = permutation[i] + permutation[i + 1]
        if s in unique_sums:
            return False

        unique_sums.add(s)

    return True


if __name__ == "__main__":
    print(count(1, 1))  # 1
    print(count(4, 2))  # 4
    print(count(8, 5))  # 830
