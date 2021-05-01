"""
Given two singly linked lists that intersect at some point,
find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, 
return the node with value 8.

In this example, assume nodes with the same value are the exact
same node objects.

Do this in O(M + N) time (where M and N are the lengths of
the lists) and constant space.
"""
from collections import deque
from time import sleep

def get_circular_next(llist, step=1):
    while step:
        current_value = llist.popleft()
        llist.append(current_value)
        step -= 1
    return current_value

def search_intersection(llist_1, llist_2):
    value_1 = get_circular_next(llist_1)
    value_2 = get_circular_next(llist_2)
    current_step = 1
    counter = 0
    while value_1 != value_2:
        if counter >= len(llist_1): current_step = 2
        value_1 = get_circular_next(llist_1)
        value_2 = get_circular_next(llist_2, step=current_step)
        counter += 1
    return value_1

# Testing
print("-"*14, "\n", ".: Testing :.", "\n", "-"*14, sep='')
test_function = search_intersection

inputs = [
    {'llist_1': deque([3,7,8,10]), 'llist_2': deque([99,1,8,10])}
]

for input_arg in inputs:
    print(f"in: {input_arg}\n|\n┖-> out: {test_function(**input_arg)}\n")