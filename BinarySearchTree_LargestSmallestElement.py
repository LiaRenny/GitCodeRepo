# This code implements a Binary Search Tree (BST)
# and finds the smallest, largest, and second largest elements in it.

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def find_smallest(root):
    current = root
    while current.left:
        current = current.left
    return current.key

def find_largest(root):
    current = root
    while current.right:
        current = current.right
    return current.key

def find_second_largest(root):
    parent = None
    current = root
    while current.right:
        parent = current
        current = current.right
    # If largest has a left subtree, second largest is the largest in that subtree
    if current.left:
        return find_largest(current.left)
    # Else, parent is the second largest
    if parent:
        return parent.key
    return None  # Only one node in tree

if __name__ == "__main__":
    arr = list(map(int, input("Enter BST elements separated by spaces: ").split()))
    root = None
    for num in arr:
        root = insert(root, num)
    print("Smallest element:", find_smallest(root))
    print("Largest element:", find_largest(root))
    second_largest = find_second_largest(root)
    if second_largest is not None:
        print("Second largest element:", second_largest)
    else:
        print("Second largest element does not exist.")