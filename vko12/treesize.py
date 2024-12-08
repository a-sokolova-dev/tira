class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class TreeSet:
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._add_recursive(self.root, value)

    def _add_recursive(self, node, value):
        if node.value == value:
            return
        elif value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._add_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._add_recursive(node.right, value)

    def __contains__(self, value):
        return self._contains_recursive(self.root, value)

    def _contains_recursive(self, node, value):
        if node is None:
            return False
        if node.value == value:
            return True
        elif value < node.value:
            return self._contains_recursive(node.left, value)
        else:
            return self._contains_recursive(node.right, value)

    def __repr__(self):
        items = []
        self._in_order_traversal(self.root, items)
        return str(items)

    def _in_order_traversal(self, node, items):
        if node:
            self._in_order_traversal(node.left, items)
            items.append(node.value)
            self._in_order_traversal(node.right, items)

    def __len__(self):
        return self._count_nodes(self.root)

    def _count_nodes(self, node):
        if node is None:
            return 0
        return 1 + self._count_nodes(node.left) + self._count_nodes(node.right)

if __name__ == "__main__":
    s = TreeSet()
    print(len(s))  # 0
    s.add(1)
    print(len(s))  # 1
    s.add(2)
    print(len(s))  # 2
    s.add(3)
    print(len(s))  # 3
    s.add(2)
    print(len(s))  # 3
