import itertools
def count(n, k, x):
    res = 0
    numbers = range(1,n+1)
    for combination in itertools.combinations(numbers,k):
        if sum(combination)==x: res+=1
    return res

if __name__ == "__main__":
    print(count(1, 1, 1)) # 1
    print(count(5, 2, 6)) # 2
    print(count(8, 3, 12)) # 6
    print(count(10, 4, 20)) # 16