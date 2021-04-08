"""
Given the root to a binary tree, implement serialize(root), which
serializes the tree into a string, and deserialize(s), which
deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(node:Node):
    if not node:
        return 'x'
    return '-'.join([node.val,f'{serialize(node.left)}',f'{serialize(node.right)}'])

def deserialize(node_series:str):
    nodes_values = node_series.split("-")
    return deserialize_helper(nodes_values)

def deserialize_helper(nodes_values):
    current_root_val = nodes_values[0]
    nodes_values = nodes_values[1:]
    
    if current_root_val == 'x':
        return None

    return Node(
        val=current_root_val,
        left=deserialize_helper(nodes_values),
        right=deserialize_helper(nodes_values)
        )


tree = Node('root', Node('left', Node('left.left')), Node('right'))
print(serialize(tree))
print("_"*10)
print(deserialize(serialize(tree)))

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'