def count(x, coins):
    min_coins = [-1] * (x + 1)
    dp = [0] * (x + 1)
    
    for coin in coins:
        if coin <= x:
            min_coins[coin] = 1
            dp[coin] = 1
    
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
                    dp[amount] += dp[amount - coin]
            
            min_coins[amount] = min_coins_prev + 1
    
    return dp[x]

if __name__ == "__main__":
    print(count(5, [1])) # 1
    print(count(5, [1, 2, 3, 4])) # 4
    print(count(13, [1, 2, 5])) # 12
    print(count(42, [1, 5, 6, 17])) # 30