"""
CSES-3116 Kolikot nopeasti

Please see my GitHub repository for used theory references and writeups:
https://github.com/a-sokolova-dev/tira/tree/main/vko9

Anna Sokolova • December 2024
"""


def count(x):
    count = 0
    coins = [5, 2, 1]
    to_exchange = x

    for coin in coins:
        count += to_exchange // coin
        left = to_exchange % coin
        to_exchange = left

    return count


if __name__ == "__main__":
    print(count(13))  # 4
    print(count(12345))  # 2469
    print(count(1337**9))  # 2730314408854633746890878156
