import itertools

def create(s):
    list = []
    for permutation in set(itertools.permutations(s)):
        list.append("".join(permutation))
    return sorted(list)

if __name__ == "__main__":
    print(create("abc")) # ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    print(create("aaaaa")) # ['aaaaa']
    print(create("abab")) # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
    print(len(create("aybabtu"))) # 1260