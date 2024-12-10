"""
CSES-3310 Pienimmät määrät

Please see my GitHub repository for used theory references and writeups:
https://github.com/a-sokolova-dev/tira/tree/main/vko10

Anna Sokolova • December 2024
"""


def count(x, coins):
    # could be most definitely simplified,
    # not sure if it makes sense to keep 2 dp arrays
    #
    # will try to revisit and resubmit this later

    # min_coins[i] stores minimum coin count to get the sum i
    min_coins = [-1] * (x + 1)
    # result[i] stores amount of ways to get get the sum i
    result = [0] * (x + 1)

    for coin in coins:
        if coin <= x:
            min_coins[coin] = 1
            result[coin] = 1

    for amount in range(1, x + 1):
        # skip if a coin denomination
        if amount in coins:
            continue

        min_coins_prev = -1
        for coin in coins:
            if amount - coin > 0 and min_coins[amount - coin] != -1:
                if min_coins_prev == -1 or min_coins[amount - coin] < min_coins_prev:
                    min_coins_prev = min_coins[amount - coin]

        if min_coins_prev != -1:
            for coin in coins:
                if amount - coin > 0 and min_coins[amount - coin] == min_coins_prev:
                    result[amount] += result[amount - coin]

            min_coins[amount] = min_coins_prev + 1

    return result[x]


if __name__ == "__main__":
    print(count(5, [1]))  # 1
    print(count(5, [1, 2, 3, 4]))  # 4
    print(count(13, [1, 2, 5]))  # 12
    print(count(42, [1, 5, 6, 17]))  # 30
