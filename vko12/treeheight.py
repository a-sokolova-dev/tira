import collections 

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
        else:
            self._add_recursive(self.root, value)

    def _add_recursive(self, node, value):
        if node.value == value:
            return
        elif value < node.value:
            if not node.left:
                node.left = Node(value)
            else:
                self._add_recursive(node.left, value)
        else:
            if not node.right:
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

    def height(self):
        if not self.root:
            return -1
        
        queue = collections.deque([(self.root, 0)])
        max_height = -1
        
        while queue:
            node, level = queue.popleft()
            max_height = max(max_height, level)
            
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        
        return max_height

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
