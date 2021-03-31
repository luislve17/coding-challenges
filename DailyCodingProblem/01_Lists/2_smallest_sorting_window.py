"""
Given an array of integers that are out of order, determine the bounds of the smallest
window that must be sorted in order for the entire array to be sorted. For example,
given [ 3 , 7 , 5 , 6 , 9] , you should return ( 1 , 3 )
"""

def locate_sorting_window(values):
    window_index = [0,len(values) - 1]
    max_value = -float('inf')
    min_value = float('inf')

    # Finding right-most window index
    for i, value in enumerate(values):
        max_value = max(value, max_value)
        # if statement checks if "value" is in a bad position
        # and needs to be considered inside the window, this
        # is because "value", while iterating from left to right
        # in the array, should not be "less than" the "max_value"
        # and be at its right
        if value < max_value:
            window_index[1] = i

    # Finding left-most window index
    for i, value in enumerate(values[::-1]):
        min_value = min(value, min_value)
        # Similarly, the "value" in iteration, while
        # checking from right to left, should not be
        # at "min_value"'s left; if so, "value" needs
        # to be considered inside the window
        if value > min_value:
            window_index[0] = len(values) - i - 1

    return window_index


# Testing
print("-"*14, "\n", ".: Testing :.", "\n", "-"*14, sep='')
inputs = [
    [ 3 , 7 , 5 , 6 , 9],
    [ 3 , 7 , 5 , 6 , 4],
    [ 3 , 7 , 5 , 6 , 9, 1],
]

for input_arg in inputs:
    print(f"in: {input_arg}\n|\n┖-> out: {locate_sorting_window(input_arg)}\n")
