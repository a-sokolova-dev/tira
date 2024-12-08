""" From the matskut """

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

    def count(self, x):
        items = []
        self.traverse(self.root, items)
        return items.count(x)

if __name__ == "__main__":
    s = TreeSet()
    s.add(4)
    s.add(1)
    s.add(2)
    s.add(1)
    print(s) # [1, 1, 2, 4]
    print(1 in s) # True
    print(2 in s) # True
    print(3 in s) # False
    print(4 in s) # True
    print(s.count(1)) # 2
    print(s.count(2)) # 1
    print(s.count(3)) # 0
    print(s.count(4)) # 1