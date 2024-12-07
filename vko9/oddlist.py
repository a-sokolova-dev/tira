import itertools

def count(n, x):
    count = 0
    t = list(range(1, n+1))
    for permutation in itertools.permutations(t):
        if valid_permutation(permutation, x):
            count += 1
    return count

def valid_permutation(permutation, x):
    if permutation[0] != x:
        return False

    unique_sums = set()

    for i in range(0, len(permutation)-1):
        s = permutation[i]+permutation[i+1]
        if s not in unique_sums:
            unique_sums.add(s)
        else: return False

    return True

if __name__ == "__main__":
    print(count(1, 1)) # 1
    print(count(4, 2)) # 4
    print(count(8, 5)) # 830