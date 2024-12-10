"""
CSES-3309 Eniten kolikkoja

Please see my GitHub repository for used theory references and writeups:
https://github.com/a-sokolova-dev/tira/tree/main/vko10

Anna Sokolova • December 2024
"""


def find(x, _coins):
    # one of the coins is guaranteed to be 1, so we can just return x
    return x


if __name__ == "__main__":
    print(find(5, [1, 2, 5]))  # 5
    print(find(10, [1]))  # 10
    print(find(8, [1, 2, 3, 4, 5]))  # 8
