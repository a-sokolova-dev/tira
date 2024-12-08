import random
import time
from collections import deque

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
    
    def height(self):
        if not self.root:
            return -1
        
        # Iterative BFS approach to calculate height
        queue = deque([(self.root, 0)])  # store node with its level (height)
        max_height = -1
        
        while queue:
            node, level = queue.popleft()
            max_height = max(max_height, level)
            
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        
        return max_height
    
    
# Testi 1: alkiot lisätään pienimmästä suurimpaan
tree1 = TreeSet()
for i in range(1, 1001):
    tree1.add(i)
height1 = tree1.height()

# Testi 2: alkiot lisätään satunnaisessa järjestyksessä
tree2 = TreeSet()
random_numbers = list(range(1, 1001))
random.shuffle(random_numbers)
for num in random_numbers:
    tree2.add(num)
height2 = tree2.height()

print(f"Korkeus testissä 1: {height1}")
print(f"Korkeus testissä 2: {height2}")
