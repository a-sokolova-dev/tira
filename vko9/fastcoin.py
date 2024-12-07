def count(x):
    coin_amount = 0
    coins = [5,2,1]
    to_exchange = x

    for coin in coins:
        coin_amount += to_exchange // coin
        left   = to_exchange % coin
        to_exchange = left

    return coin_amount


if __name__ == "__main__":
    print(count(13)) # 4
    print(count(12345)) # 2469
    print(count(1337**9)) # 2730314408854633746890878156