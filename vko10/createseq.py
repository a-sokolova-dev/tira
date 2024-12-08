# simplified cycles
def find(t):
    if not t: return []

    n = len(t)
    lenghts = [1] * n
    prev = list(range(n))

    for i in range(1, n):
        for j in range(i):
            if (t[i] > t[j] and 
                lenghts[i] < lenghts[j] + 1):
                lenghts[i] = lenghts[j] + 1
                prev[i] = j
    
    max_idx = lenghts.index(max(lenghts))
    
    result = []
    curr_idx = max_idx
    
    while True:
        result.append(t[curr_idx])
        if curr_idx == prev[curr_idx]:
            break
        curr_idx = prev[curr_idx]
    
    return result[::-1]
 
if __name__ == "__main__":
    print(find([1, 1, 2, 2, 3, 3])) # [1, 2, 3]
    print(find([1, 1, 1, 1])) # [1]
    print(find([5, 4, 3, 2, 1])) # [3]
    print(find([4, 1, 5, 6, 3, 4, 1, 8])) # [1, 3, 4, 8]