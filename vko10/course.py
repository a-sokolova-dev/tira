"""
CSES-3137 Kurssi

Please see my GitHub repository for used theory references and writeups:
https://github.com/a-sokolova-dev/tira/tree/main/vko10

Anna Sokolova • December 2024
"""


import math


def count(x):
    # cool problem! really enjoyed it, took me some time to figure out.
    # could be further optimized to use dp for memoization
    # instead of recursion, but the principal remains the same.

    if x < 40 or x > 64:
        return 0

    weeks = 8
    min_t = 5
    max_t = 8

    def solve(tasks, w):
        if w > weeks:
            return 0
        if tasks < 0:
            return 0
        if (tasks == 0 and w == weeks):
            return 1

        count = 0
        for t in range(min_t, max_t + 1):
            count += math.comb(max_t, t) * solve(tasks - t, w + 1)

        return count

    return solve(x, 0) * math.factorial(x)

if __name__ == "__main__":
    print(count(40)) # 78913132667888442497725132524762783866832203758436352000000000
    print(count(55)) # 320424698352073967965876852452014215914220727801318938295395908593909760000000000000
    print(count(64)) # 126886932185884164103433389335161480802865516174545192198801894375214704230400000000000000
    print(count(100)) # 0