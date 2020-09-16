"""
The code below generates a given number of random strings that consists of numbers and lower case English letters. You can also define the range of the variable lengths of the strings being generated.

The code is functional but has a lot of room for improvement. Use what you have learned about simple and efficient code, refactor the code.
"""

import random
import sys

CHAR_POOL = [chr(n) for n in range(48, 58)] + [chr(n) for n in range(97, 123)]

def batch_string_generator(n, a=8, b=12):
    if a > b:
        sys.exit('Incorrect min and max string lengths. Try again.')
    r = []
    for i in range(n):
        length = random.choice(range(a, b))
        string = "".join(random.choices(CHAR_POOL, k=length))
        r.append(string)
    return r

a = int(input('Enter minimum string length: '))
b = int(input('Enter maximum string length: '))
n = int(input('How many random strings to generate? '))

print(batch_string_generator(n, a, b))