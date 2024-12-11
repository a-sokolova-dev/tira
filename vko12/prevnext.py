"""
CSES-3170 Edellinen ja seuraava

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

    def next(self, x):
        node = self.root
        prev_min = None
        while node != None:
            if node.value > x:
                if prev_min is None or node.value < prev_min:
                    prev_min = node.value
                node = node.left
            else:
                node = node.right

        return prev_min

    def prev(self, x):
        node = self.root
        prev_max = None
        while node != None:
            if node.value < x:
                if prev_max is None or node.value > prev_max:
                    prev_max = node.value
                node = node.right
            else:
                node = node.left

        return prev_max


if __name__ == "__main__":
    s = TreeSet()
    s.add(2)
    s.add(5)
    print(s.prev(5))  # 2
    print(s.prev(2))  # None
    print(s.next(1))  # 2
    print(s.next(2))  # 5
    print(s.next(5))  # None
