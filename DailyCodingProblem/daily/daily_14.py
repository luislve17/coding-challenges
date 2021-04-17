"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.
"""
import random

def monte_carlo_pi():
    out_counter = 0
    in_counter = 0
    estimated_pi = float("Inf")
    PI = 3.1415
    while(abs(estimated_pi - PI) > 0.0001):
        x, y = random.random(), random.random()
        r_squared = x**2 + y**2
        if r_squared <= 1: in_counter += 1
        else: out_counter += 1
        estimated_pi = 4.0*(in_counter/(in_counter + out_counter)) 
        print(estimated_pi)

    return estimated_pi


# Testing
print("-"*14, "\n", ".: Testing :.", "\n", "-"*14, sep='')
test_function = monte_carlo_pi

inputs = [
    {}
]

for input_arg in inputs:
    print(f"in: {input_arg}\n|\n┖-> out: {test_function(**input_arg)}\n")