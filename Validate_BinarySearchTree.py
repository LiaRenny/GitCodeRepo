# Validate Binary Search Tree

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def build_tree(values):
    if not values or values[0] is None:
        return None
    nodes = [Node(val) if val is not None else None for val in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root

def is_valid_bst(node, min_val=float('-inf'), max_val=float('inf')):
    if node is None:
        return True
    if not (min_val < node.key < max_val):
        return False
    return (is_valid_bst(node.left, min_val, node.key) and
            is_valid_bst(node.right, node.key, max_val))

if __name__ == "__main__":
    # Example input: 10 5 15 None None 12 20
    raw = input("Enter tree nodes in level order (use None for missing): ").split()
    arr = [int(x) if x != "None" else None for x in raw]
    root = build_tree(arr)
    if is_valid_bst(root):
        print("The tree is a valid BST.")
    else:
        print("The tree is NOT a valid BST.")