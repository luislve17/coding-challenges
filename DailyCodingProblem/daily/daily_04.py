"""
Given an array of integers, find the first missing positive
integer in linear time and constant space. In other words,
find the lowest positive integer that does not exist in the
array. The array can contain duplicates and negative numbers
as well.

For example, the input [3, 4, -1, 1] should give 2.
The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""

def indexing_sorting(integers):
    for i in range(len(integers)):
        while integers[i] != (i+1):
            j = integers[i] - 1
            if j < 0 or j >= len(integers): break
            integers[i], integers[j] = integers[j], integers[i]

    return integers

# Testing
print("-"*14, "\n", ".: Testing :.", "\n", "-"*14, sep='')
test_function = indexing_sorting
inputs = [
    {'integers': [3,4,-1,1]}
]

for input_arg in inputs:
    print(f"in: {input_arg}\n|\n┖-> out: {test_function(**input_arg)}\n")
