def count_sequences(n, result=None):
    if result is None:
        result = [0] * (n + 1)
    result[0] = 1
    
    for j in range(2, n + 1, 2):
        count = 0
        for i in range(2, j + 1, 2):
            count += result[i - 2] * result[j - i]
        result[j] = count
    
    return result[n]

print(count_sequences(100))