"""
CSES-3147 Pienet summat

Please see my GitHub repository for used theory references and writeups:
https://github.com/a-sokolova-dev/tira/tree/main/vko11

Anna Sokolova • December 2024
"""


import heapq


class SubsetNode:
    # Used the general idea proposed by David Eisenstat here:
    # https://stackoverflow.com/questions/33219712/find-k-th-minimum-sum-of-every-possible-subset
    # Modified for storing subsets and accounting for the empty set
    def __init__(self,
                 max_elem=0,
                 subset=None,
                 subset_sum=0):
        # storing max element, current subset and subset sum
        self.max_elem = max_elem
        self.subset = subset or set()
        self.subset_sum = subset_sum

    def generate_children(self):
        if not self.subset:
            yield SubsetNode(max_elem=1, subset={1}, subset_sum=1)
            return

        if self.max_elem < 10**9:
            next_elem = self.max_elem + 1

            child1_subset = self.subset.copy()
            child1_subset.remove(self.max_elem)
            child1_subset.add(next_elem)

            child1 = SubsetNode(
                max_elem=next_elem,
                subset=child1_subset,
                # avoid calling sum() by carefully substracting & adding
                subset_sum=self.subset_sum - self.max_elem + next_elem
            )
            yield child1

        if self.max_elem < 10**9:
            next_elem = self.max_elem + 1
            child2_subset = self.subset.copy()
            child2_subset.add(next_elem)

            child2 = SubsetNode(
                max_elem=next_elem,
                subset=child2_subset,
                # avoid calling sum() by carefully substracting & adding
                subset_sum=self.subset_sum + next_elem
            )
            yield child2

    def __lt__(self, other):
        return self.subset_sum < other.subset_sum

    # for debugging
    def __str__(self):
        return f"Subset: {self.subset}, Sum: {self.subset_sum}, Max: {self.max_elem}"


def find(k: int):
    root = SubsetNode()
    q = [root]
    heapq.heapify(q)

    for _ in range(k - 1):
        # get and remove the current minimum subset node
        current = heapq.heappop(q)
        for child in current.generate_children():
            heapq.heappush(q, child)

    final_subset = heapq.heappop(q)
    return final_subset.subset_sum


if __name__ == "__main__":
    print(find(1))  # 0
    print(find(2))  # 1
    print(find(3))  # 2
    print(find(4))  # 3
    print(find(5))  # 3
    print(find(123))  # 15
    print(find(123456))  # 62
