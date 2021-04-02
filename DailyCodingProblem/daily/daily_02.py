"""
Given an array of integers, return a new array such that each element
at index i of the new array is the product of all the numbers in the
original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would
be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output
would be [2, 3, 6]
"""


from functools import reduce

def items_product(numeric_list):
    products = []
    for i, value in enumerate(numeric_list):
        curated_numeric_list = numeric_list[0:i] + numeric_list[i+1:]
        products.append(reduce( (lambda x,y: x*y) , curated_numeric_list))

    return products

# Testing
print("-"*14, "\n", ".: Testing :.", "\n", "-"*14, sep='')
test_function = items_product
inputs = [
    {'numeric_list': list(range(1,6))},
    {'numeric_list': list(range(2,8,2))},
    {'numeric_list': [3,2,1]},
]

for input_arg in inputs:
    print(f"in: {input_arg}\n|\n┖-> out: {test_function(**input_arg)}\n")
