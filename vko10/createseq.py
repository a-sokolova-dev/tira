"""
CSES-3126 Alijonon muodostus

Please see my GitHub repository for used theory references and writeups:
https://github.com/a-sokolova-dev/tira/tree/main/vko10

Anna Sokolova • December 2024
"""


def find(t):
    n = len(t)
    if (n == 1):
        return t
    prev = {}

    for i in range(n):
        prev[i] = [t[i]]
        for j in range(i):
            if t[i] > t[j]:
                curr = prev[j] + [t[i]]
                if len(curr) > len(prev[i]):
                    prev[i] = curr

    result = []
    for i in range(1, n):
        if len(prev[i]) > len(result):
            result = prev[i]

    return result


if __name__ == "__main__":
    print(find([1, 1, 2, 2, 3, 3]))  # [1, 2, 3]
    print(find([1, 1, 1, 1]))  # [1]
    print(find([5, 4, 3, 2, 1]))  # [3]
    print(find([4, 1, 5, 6, 3, 4, 1, 8]))  # [1, 3, 4, 8]
    print(find([10]))  # [1, 3, 4, 8]
