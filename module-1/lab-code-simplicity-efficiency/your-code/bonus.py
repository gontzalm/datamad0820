"""
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

For example, if the stair has 4 steps, there are 5 ways to climb to the top:
1) 1, 1, 1, 1
2) 1, 2, 1
3) 1, 1, 2
4) 2, 1, 1
5) 2, 2

The following class calculates the total ways to climb a stair with the specified number of steps.
It also counts the number of calculations performed which indicates the efficiency of the code.
Try if you can improve the performance of the code.
"""

from itertools import permutations
from math import sqrt

def fibonacci(n):
    """Return the nth element in the fibonacci series"""
    return int(1/sqrt(5)*((1 + sqrt(5)) / 2)**n + 0.5)

class ClimbStairs:
    """
    Class constructor
    total_steps: how many steps in total in the stair
    """
    def __init__(self, total_steps=10): 
        self.total_steps = total_steps
        self.calculation_count = 0

    """
    This function calculates how many solutions are there to reach the top when I am currently at the ith step
    i - the step I am currently at
    """
    def calc_solutions(self): 
        self.calculation_count += 1
        return fibonacci(self.total_steps + 1)

    def get_calculation_count(self):
        return self.calculation_count

    def solve(self):
        return self.calc_solutions()

total_steps = int(input("How many steps in the stair? "))
new_challenge = ClimbStairs(total_steps)
print(f"Ways to climb to top: {new_challenge.solve()}")
print(f"Total calculations performed: {new_challenge.get_calculation_count()}")
