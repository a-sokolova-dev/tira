"""
CSES-3117 Lisää kolikoita

Please see my GitHub repository for used theory references and writeups:
https://github.com/a-sokolova-dev/tira/tree/main/vko9

Anna Sokolova • December 2024
"""


def count(x):
    if (x < 4):
        return x

    fives_amount = x // 5
    left = x % 5

    # if can't exchange with 4's
    if (left == 2 and x < 10):
        extra_coins = 2
    elif left == 0:
        extra_coins = 0
    else:
        extra_coins = 1

    return fives_amount + extra_coins


if __name__ == "__main__":
    print(count(8))  # 2
    print(count(12345))  # 2469
    print(count(1337 ** 9))  # 2730314408854633746890878156
