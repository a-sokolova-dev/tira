class Node:
    def __init__(self, value, parent=None):
        self.value = value
        self.left = None
        self.right = None
        self.height = 0

class TreeSet:
    def __init__(self):
        self.root = None

    def add(self, value):
        if not self.root:
            self.root = Node(value)
            return

        node = self.root
        path = []
        while True:
            path.append(node)
            if node.value == value:
                return
            if node.value > value:
                if not node.left:
                    node.left = Node(value)
                    path.append(node.left)
                    self.check(path)
                    return
                else:
                    node = node.left
            else:
                if not node.right:
                    node.right = Node(value)
                    path.append(node.right)
                    self.check(path)
                    return
                else:
                    node = node.right

    def height(self, node):
        return node.height if node else -1
 
    def fix_parent(self, parent, old_node, new_node):
        if not parent:
            self.root = new_node
            return
        if parent.left == old_node:
            parent.left = new_node
        else:
            parent.right = new_node

    def update_height(self, node):
        node.height = max(self.height(node.left), self.height(node.right)) + 1

    def check(self, path):
        for i in range(len(path) - 1, -1, -1):
            x = path[i]
            self.update_height(x)
            if abs(self.height(x.left) - self.height(x.right)) > 1:
                p = path[i - 1] if i > 0 else None
                y = path[i + 1]
                z = path[i + 2]
                if x.left == y and y.left == z:
                    self.rotate_right(p, x, y)
                elif x.right == y and y.right == z:
                    self.rotate_left(p, x, y)
                elif x.left == y and y.right == z:
                    self.rotate_left(x, y, z)
                    self.rotate_right(p, x, z)
                elif x.right == y and y.left == z:
                    self.rotate_right(x, y, z)
                    self.rotate_left(p, x, z)
                    
    def rotate_left(self, parent, x, y):
        x.right = y.left
        y.left = x
        self.fix_parent(parent, x, y)
        self.update_height(x)
        self.update_height(y)
            
    def rotate_right(self, parent, x, y):
        x.left = y.right
        y.right = x
        self.fix_parent(parent, x, y)
        self.update_height(x)
        self.update_height(y)

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