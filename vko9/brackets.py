"""
CSES-3118 Sulkulausekkeet

Please see my GitHub repository for used theory references and writeups:
https://github.com/a-sokolova-dev/tira/tree/main/vko9

Anna Sokolova • December 2024
"""


import itertools


def count(n, k):
    total_combinations = 0
    for sequence in itertools.product("()", repeat=n):
        if valid(sequence, k):
            total_combinations += 1
    return total_combinations


def valid(sequence, k):
    depth = 0

    for bracket in sequence:
        if bracket == "(":
            depth += 1
        if bracket == ")":
            depth -= 1
        if depth < 0 or depth > k:
            return False

    return depth == 0


if __name__ == "__main__":
    print(count(6, 1))  # 1
    print(count(6, 2))  # 4
    print(count(6, 3))  # 5
    print(count(9, 1))  # 0
    print(count(16, 4))  # 1094
