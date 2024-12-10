"""
CSES-3127 Kaikki alijonot

Please see my GitHub repository for used theory references and writeups:
https://github.com/a-sokolova-dev/tira/tree/main/vko10

Anna Sokolova • December 2024
"""


def count(t):
    result = {}

    for i in range(len(t)):
        result[i] = 1
        for j in range(i):
            if t[j] < t[i]:
                result[i] += result[j]

    return sum([result[i] for i in range(len(t))])


if __name__ == "__main__":
    print(count([1, 1, 2, 2, 3, 3]))  # 26
    print(count([1, 1, 1, 1]))  # 4
    print(count([5, 4, 3, 2, 1]))  # 5
    print(count([4, 1, 5, 6, 3, 4, 1, 8]))  # 37
