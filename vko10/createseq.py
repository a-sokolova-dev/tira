def find(t):
    n = len(t)
    lis = [1]*n

    prev = [0]*n
    for i in range(0, n):
        prev[i] = i

    for i in range (1 , n):
        for j in range(0 , i):
            if t[i] > t[j] and lis[i]< lis[j] + 1:
                lis[i] = lis[j]+1
                prev[i] = j

    maximum = 0
    idx = 0

    for i in range(n):
        if maximum < lis[i]:
            maximum = lis[i]
            idx = i

    seq = [t[idx]]
    while idx != prev[idx]:
        idx = prev[idx]
        seq.append(t[idx])

    return seq[::-1]

if __name__ == "__main__":
    print(find([1, 1, 2, 2, 3, 3])) # [1, 2, 3]
    print(find([1, 1, 1, 1])) # [1]
    print(find([5, 4, 3, 2, 1])) # [3]
    print(find([4, 1, 5, 6, 3, 4, 1, 8])) # [1, 3, 4, 8]