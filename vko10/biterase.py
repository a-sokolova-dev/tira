def count(s, memo={}):
    if s in memo:
        return memo[s]
    if len(s) == 0:
        return 1

    counts = 0
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            counts += count(s[:i] + s[i+2:])

    memo[s] = counts
    return counts

if __name__ == "__main__":
    print(count("1001")) # 2
    print(count("1100")) # 1
    print(count("101100")) # 5
    print(count("11001")) # 0
    print(count("01110100100110")) # 6027
    print(count("011101001000111010010001110100100")) # yes