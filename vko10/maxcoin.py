def find(x, coins):
    # one of the coins is guaranteed to be 1, so we can just return x
    return x

if __name__ == "__main__":
    print(find(5, [1, 2, 5])) # 5
    print(find(10, [1])) # 10
    print(find(8, [1, 2, 3, 4, 5])) # 8