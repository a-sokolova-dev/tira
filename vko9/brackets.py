import itertools

def count(n, k):
    total_combinations = 0
    for sequence in itertools.product("()", repeat=n):
        if valid_combination(sequence, k):
            total_combinations += 1
    return total_combinations

def valid_combination(sequence, k):
    depth = 0
    max_depth = 0

    for bracket in sequence:
        if bracket == "(":
            depth += 1
            max_depth = max(max_depth, depth)
        if bracket == ")":
            depth -= 1

        if depth < 0 or max_depth > k:
                return False
        
    return depth == 0

if __name__ == "__main__":
    print(count(6, 1)) # 1
    print(count(6, 2)) # 4
    print(count(6, 3)) # 5
    print(count(9, 1)) # 0
    print(count(16, 4)) # 1094