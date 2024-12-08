import time, math

def own_function(n):
    multiplier = 1 / (n // 2 + 1)
    binomikerroin = math.comb(n, n // 2)
    
    return int(multiplier * binomikerroin)


def count_sequences(n, d=0, result={}):
    if d < 0 or d > n:
        return 0
    if n == 0:
        return 1
    if (n, d) not in result:
        result[(n, d)] = count_sequences(n - 1, d + 1) + \
                         count_sequences(n - 1, d - 1)
    return result[(n, d)]

# testing times

t1 = time.time()
for k in range(100, 1000, 100):
    print(k, own_function(k))
t2 = time.time()

print("own_function time: ", t2 - t1)


t1 = time.time()
for k in range(100, 1000, 100):
    print(k, count_sequences(k))
t2 = time.time()

print("count_sequences time: ", t2 - t1)