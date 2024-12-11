"""
CSES-3168 Pienin ja suurin

Please see my GitHub repository for used theory references and writeups:
https://github.com/a-sokolova-dev/tira/tree/main/vko12

Anna Sokolova • December 2024
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class TreeSet:
    def __init__(self):
        self.root = None

    def add(self, value):
        if not self.root:
            self.root = Node(value)
            return

        node = self.root
        while True:
            if node.value == value:
                return
            if node.value > value:
                if not node.left:
                    node.left = Node(value)
                    return
                node = node.left
            else:
                if not node.right:
                    node.right = Node(value)
                    return
                node = node.right

    def __contains__(self, value):
        if not self.root:
            return False

        node = self.root
        while node:
            if node.value == value:
                return True
            if node.value > value:
                node = node.left
            else:
                node = node.right

        return False

    def __repr__(self):
        items = []
        self.traverse(self.root, items)
        return str(items)

    def traverse(self, node, items):
        if not node:
            return
        self.traverse(node.left, items)
        items.append(node.value)
        self.traverse(node.right, items)

    def min(self):
        prev_value = None
        node = self.root

        while node:
            prev_value = node.value
            node = node.left

        return prev_value

    def max(self):
        prev_value = None
        node = self.root

        while node:
            prev_value = node.value
            node = node.right

        return prev_value


if __name__ == "__main__":
    s = TreeSet()
    print(s.min())  # None
    print(s.max())  # None
    s.add(1)
    s.add(2)
    s.add(3)
    print(s.min())  # 1
    print(s.max())  # 3
