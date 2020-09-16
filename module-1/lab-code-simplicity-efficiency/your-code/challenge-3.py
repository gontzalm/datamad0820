"""
You are presented with an integer number larger than 5. Your goal is to identify the longest side possible in a right triangle whose sides are not longer than the number you are given.

For example, if you are given the number 15, there are 3 possibilities to compose right triangles:

1. [3, 4, 5]
2. [6, 8, 10]
3. [5, 12, 13]

The following function shows one way to solve the problem but the code is not ideal or efficient.
Refactor the code based on what you have learned about code simplicity and efficiency.
"""
from itertools import combinations

def largest_right_side(max_side):
    solutions = []
    for comb in combinations(range(5, max_side), 3):
        # sort comb in order to extract largest value
        comb = sorted(list(comb), reverse=True)
        h, k1, k2 = comb
        if h**2 == k1**2 + k2**2:
            solutions.append(h)
    return max(solutions)

prompt = "What is the maximal length of the triangle side? Enter a number: "
try:
    max_side = int(input(prompt))
    if max_side <= 5:
        raise Exception("Please enter an integer greater than 5.")
except Exception as e:
    print(e)
else:
    print(f"The longest side possible is {largest_right_side(max_side)}")