"""
cons(a, b) constructs a pair, and car(pair) and
cdr(pair) returns the first and last element of
that pair. For example, car(cons(3, 4)) returns 3,
and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
Implement car and cdr.
"""

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair_f):
    return pair_f(lambda x,y: x)

def cdr(pair_f):
    return pair_f(lambda  x,y: y)

# Testing
print("-"*14, "\n", ".: Testing :.", "\n", "-"*14, sep='')
test_function_1 = car
test_function_2 = cdr
inputs = [
    {'pair_f': cons(3,4)},
]

for input_arg in inputs:
    print(f"in: {input_arg}\n|\n┖-> out: {test_function_1(**input_arg)}\n")
    print(f"in: {input_arg}\n|\n┖-> out: {test_function_2(**input_arg)}\n")

