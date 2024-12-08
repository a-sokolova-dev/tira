def count(x, coins):
    C1 = {c:1 for c in coins}
    C2  = {c:1 for c in coins}
    for s in range(1,x+1):
        if s in coins: continue
        mincoin_prev = min([C1[s-c] for c in coins if s-c>0])
        C2[s] = sum([C2[s-c] for c in coins if s-c>0 and C1[s-c]==mincoin_prev])
        C1[s] = mincoin_prev + 1
    return C2[x]
        

if __name__ == "__main__":
    print(count(5, [1])) # 1
    print(count(5, [1, 2, 3, 4])) # 4
    print(count(13, [1, 2, 5])) # 12
    print(count(42, [1, 5, 6, 17])) # 30