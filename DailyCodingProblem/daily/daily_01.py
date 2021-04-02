"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
"""

def two_items_adding(to, inside_list):
    complement_map = {}

    for value in inside_list:
        complement_map[value] = to - value
        complement_value = complement_map.get(value)
        
        if complement_value in complement_map:
            return (value, complement_map[value])



# Testing
print("-"*14, "\n", ".: Testing :.", "\n", "-"*14, sep='')
inputs = [
    {"to": 17, 'inside_list': [10, 15, 3, 7]}
]

test_function = two_items_adding

for input_arg in inputs:
    print(f"in: {input_arg}\n|\n┖-> out: {test_function(**input_arg)}\n")
