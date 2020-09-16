"""
This is a dumb calculator that can add and subtract whole numbers from zero to five.
When you run the code, you are prompted to enter two numbers (in the form of English
word instead of number) and the operator sign (also in the form of English word).
The code will perform the calculation and give the result if your input is what it
expects.

The code is very long and messy. Refactor it according to what you have learned about
code simplicity and efficiency.
"""

import operator

NUMBERS = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
}

OPERATORS = {
    "plus": operator.add,
    "minus": operator.sub,
}

print('Welcome to this calculator!')
print('It can add and subtract whole numbers from zero to five')
try:
    a = input('Please choose your first number (zero to five): ')
    b = input('What do you want to do? plus or minus: ')
    c = input('Please choose your second number (zero to five): ')
    if a not in NUMBERS or c not in NUMBERS or b not in OPERATORS:
        raise Exception("I am not able to answer this question. Check your input.")
except Exception as e:
    print(e)
else:
    res = OPERATORS[b](NUMBERS[a], NUMBERS[c])
    print(f"{a} {b} {c} equals {res}")
finally:
    print("Thanks for using this calculator, goodbye :)")