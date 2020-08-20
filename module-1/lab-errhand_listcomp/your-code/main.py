import math
import os
import random
import sys

def heading(num):
    print(f"Exercise {num}".center(80, "-"))

ex_gen = (i for i in range(1, 100))

#1. Calculate the square number of the first 20 numbers. Use square as the name of the list.
# Remember to use list comprehensions and to print your results
heading(next(ex_gen))

square = [i**2 for i in range(1, 21)]
print(square)

#2. Calculate the first 50 power of two. Use power_of_two as the name of the list.
# Remember to use list comprehensions and to print your results
heading(next(ex_gen))

power_of_two = [2**i for i in range(50)]
print(power_of_two)

#3. Calculate the square root of the first 100 numbers. Use sqrt as the name of the list.
# You will probably need to install math library with pip and import it in this file.  
# Remember to use list comprehensions and to print your results
heading(next(ex_gen))

sqrt = [math.sqrt(i) for i in range(1, 100)]
print(sqrt)

#4. Create this list [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0]. Use my_list as the name of the list.
# Remember to use list comprehensions and to print your results
heading(next(ex_gen))

my_list = [i for i in range(-10, 1)]
print(my_list)

#5. Find the odd numbers from 1-100. Use odds as the name of the list. 
# Remember to use list comprehensions and to print your results
heading(next(ex_gen))

odds = [i for i in range(1, 100) if i % 2]
print(odds)

#6. Find all of the numbers from 1-1000 that are divisible by 7. Use divisible_by_seven as the name of the list.
# Remember to use list comprehensions and to print your results
heading(next(ex_gen))

divisible_by_seven = [i for i in range(1, 1000) if i % 7 == 0]
print(divisible_by_seven)

#7. Remove all of the vowels in a string. Hint: make a list of the non-vowels. Use non_vowels as the name of the list.
# Remember to use list comprehensions and to print your results
# You can use the following test string but feel free to modify at your convenience
heading(next(ex_gen))

vowels = "aeiou"
teststring = 'Find all of the words in a string that are monosyllabic'
non_vowels = "".join([char for char in teststring if char.lower() not in vowels])
print(non_vowels)

#8. Find the capital letters (and not white space) in the sentence 'The Quick Brown Fox Jumped Over The Lazy Dog'. 
# Use capital_letters as the name of the list.  
# Remember to use list comprehensions and to print your results
heading(next(ex_gen))

sentence = "The Quick Brown Fox Jumped Over The Lazy Dog"
capital_letters = [char for char in sentence if char.isupper()]
print(capital_letters)

#9. Find all the consonants in the sentence 'The quick brown fox jumped over the lazy dog'.
# Use consonants as the name of the list.
# Remember to use list comprehensions and to print your results.
heading(next(ex_gen))

consonants = [char for char in sentence if (char not in vowels) and not char.isspace()]
print(consonants)

#10. Find the folders you have in your madrid-oct-2018 local repo. Use files as name of the list.  
# You will probably need to import os library and some of its modules. You will need to make some online research.
# Remember to use list comprehensions and to print your results.
heading(next(ex_gen))

repo = os.getcwd()
for i in range(2):
    repo = os.path.dirname(repo) # navigate 4 times to parent directory

files = os.listdir(repo)
print(files)

#11. Create 4 lists of 10 random numbers between 0 and 100 each. Use random_lists as the name of the list. 
#You will probably need to import random module
# Remember to use list comprehensions and to print your results
heading(next(ex_gen))

random_list = [random.sample(range(101), k=4) for i in range(3)]
print(random_list)

#12. Flatten the following list of lists. Use flatten_list as the name of the output.
# Remember to use list comprehensions and to print your results
heading(next(ex_gen))

list_of_lists = [[1,2,3],[4,5,6],[7,8,9]]
flatten_list = [i for lst in list_of_lists for i in lst]
print(flatten_list)

#13. Convert the numbers of the following nested list to floats. Use floats as the name of the list. 
# Remember to use list comprehensions and to print your results.
heading(next(ex_gen))

list_of_lists = [['40', '20', '10', '30'], ['20', '20', '20', '20', '20', '30', '20'], \
['30', '20', '30', '50', '10', '30', '20', '20', '20'], ['100', '100'], ['100', '100', '100', '100', '100'], \
['100', '100', '100', '100']]

floats = [float(i) for lst in list_of_lists for i in lst] 
print(floats)

#14. Handle the exception thrown by the code below by using try and except blocks. 
heading(next(ex_gen))

try:
    for i in ['a','b','c']:
        print(i**2)
except:
    print("Exception catched!!")

#15. Handle the exception thrown by the code below by using try and except blocks. 
#Then use a finally block to print 'All Done.'
# Check in provided resources the type of error you may use. 
heading(next(ex_gen))

x = 5
y = 0
try:
    z = x/y
except ZeroDivisionError as e:
    print(e)
finally:
    print("All Done")

#16. Handle the exception thrown by the code below by using try and except blocks. 
# Check in provided resources the type of error you may use. 
heading(next(ex_gen))

abc=[10,20,20]
try:
    print(abc[3])
except IndexError as e:
    print(e)

#17. Handle at least two kind of different exceptions when dividing a couple of numbers provided by the user. 
# Hint: take a look on python input function. 
# Check in provided resources the type of error you may use. 
heading(next(ex_gen))

print("Program to divide two numbers")
try:
    a = float(input("First Number: "))
    b = float(input("Second Number: "))
    print(f"Result: {a/b}")
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)

#18. Handle the exception thrown by the code below by using try and except blocks. 
# Check in provided resources the type of error you may use. 
heading(next(ex_gen))

try:
    f = open('testfile','r')
    f.write('Test write this')
except FileNotFoundError as e:
    print(e)

#19. Handle the exceptions that can be thrown by the code below using try and except blocks. 
#Hint: the file could not exist and the data could not be convertable to int
heading(next(ex_gen))

try:
    fp = open('myfile.txt')
    line = f.readline()
    i = int(s.strip())
except FileNotFoundError as e:
    print(e)
except ValueError as e:
    print(e)

#20. The following function can only run on a Linux system. 
# The assert in this function will throw an exception if you call it on an operating system other than Linux. 
# Handle this exception using try and except blocks. 
# You will probably need to import sys 
heading(next(ex_gen))

def linux_interaction():
    try:
        assert 'mac' in sys.platform, "MacOS sucks. Function can only run on Linux systems."
        print('Doing something.')
    except AssertionError as e:
        print(e)

# Bonus Questions:

# You will need to make some research on dictionary comprehension to solve the following questions

#21.  Write a function that asks for an integer and prints the square of it. 
# Hint: we need to continually keep checking until we get an integer.
# Use a while loop with a try,except, else block to account for incorrect inputs.
heading(next(ex_gen))

while True:
    try:
        num = float(input("Input integer number: ")) # will throw a ValueError if it is not numeric
        if not num.is_integer():
            raise TypeError
    except ValueError:
        print("Integers only")
    except TypeError:
        print("Integers only")
    else:
        print(f"Square: {num**2}")
        break

# 22. Find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9). 
# Use results as the name of the list 
heading(next(ex_gen))

def is_divisible(num):
    div = [num % i == 0 for i in range(2, 10)]
    return True if True in div else False

results = [i for i in range(1, 1001) if is_divisible(i)]
print(results)

# 23. Define a customised exception to handle not accepted values. 
# You have the following user inputs and the Num_of_sections can not be less than 2.
# Hint: Create a class derived from the pre-defined Exception class in Python
heading(next(ex_gen))

class MyError(Exception):
    """My customized exception"""

    def print_msg(self):
        print("Num of sections cannot be less than 2")


Total_Marks = int(input("Enter Total Marks Scored: ")) 
Num_of_Sections = int(input("Enter Num of Sections: "))

try:
    if Num_of_Sections < 2:
        raise MyError
except MyError as e:
    e.print_msg()