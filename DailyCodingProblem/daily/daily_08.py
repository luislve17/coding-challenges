"""
A unival tree (which stansfor "universal value") is a
tree where all nodes under it have the same value.

Given the root to a binary tree, count the number
of unival subtrees.

For example, the following tree has 5 unival
subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def count_unival_subtrees(tree:Node):
    return count_univals(tree)

def is_unival(root):
    if root is None:
        return True
    if root.left is not None and (root.left.val != root.val):
        return False
    if root.right is not None and (root.right.val != root.val):
        return False
    if is_unival(root.right) and is_unival(root.left):
        return True
    return False

def count_univals(root):
    if root is None:
        return 0
    total_count = count_univals(root.left) + count_univals(root.right)
    if is_unival(root):
        total_count += 1
    return total_count

# Testing
print("-"*14, "\n", ".: Testing :.", "\n", "-"*14, sep='')
test_function = count_unival_subtrees

inputs = [
    {'tree': Node("0", Node("1"), Node("0", Node("1", Node("1"), Node("1")), Node("0")))}
]

for input_arg in inputs:
    print(f"in: {input_arg}\n|\n┖-> out: {test_function(**input_arg)}\n")