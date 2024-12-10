"""
CSES-3144 Koko kierros

Please see my GitHub repository for used theory references and writeups:
https://github.com/a-sokolova-dev/tira/tree/main/vko11

Anna Sokolova • December 2024
"""


def count(n):
    if n == 1:
        return 0
    if n % 2 == 0:
        return n

    res = int((n + 1) / 2) * int((n - 1) / 2)
    return res


if __name__ == "__main__":
    print(count(2))  # 2
    print(count(5))  # 6
    print(count(31))  # 240
    print(count(1234567))  # 381038919372
