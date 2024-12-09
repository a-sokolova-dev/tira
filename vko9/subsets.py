"""
CSES-3120 Osajoukot

Please see my GitHub repository for used theory references and writeups:
https://github.com/a-sokolova-dev/tira/tree/main/vko9

Anna Sokolova • December 2024
"""


import itertools


def create(t):
    subsets_sums = []
    for i in range(len(t) + 1):
        for combination in itertools.combinations(t, i):
            subsets_sums.append(sum(combination))
    return sorted(subsets_sums)


if __name__ == "__main__":
    print(create([1, 2, 3]))  # [0, 1, 2, 3, 3, 4, 5, 6]
    print(create([42, 1337]))  # [0, 42, 1337, 1379]
    print(create([1, 1, 1]))  # [0, 1, 1, 1, 2, 2, 2, 3]
    print(create([5]))  # [0, 5]
