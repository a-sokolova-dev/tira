"""
CSES-3165 Puun korkeus

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
     # from the course material
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
        self._in_order_traversal(self.root, items)
        return str(items)

    def height(self):
        # can be also solved using a queue
        # to avoid recursion entirely
        def traverse(root):
            if root is None:
                return -1

            left_height = traverse(root.left)
            right_height = traverse(root.right)
            return max(left_height, right_height) + 1

        return traverse(self.root)


if __name__ == "__main__":
    s = TreeSet()
    print(s.height())  # -1
    s.add(2)
    print(s.height())  # 0
    s.add(1)
    print(s.height())  # 1
    s.add(3)
    print(s.height())  # 1
    s.add(4)
    print(s.height())  # 2
