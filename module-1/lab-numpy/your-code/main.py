#1. Import the NUMPY package under the name np.

import numpy as np

#2. Print the NUMPY version and the configuration.

print(np.__version__)

#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?

rng = np.random.default_rng()
a = rng.random((2, 3, 5))

#4. Print a.

print(a)

#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"

b = np.ones((5, 2, 3))

#6. Print b.

print(b)

#7. Do a and b have the same size? How do you prove that in Python code?

print(a.size == b.size)

#8. Are you able to add a and b? Why or why not?

try:
        a + b # shapes are not compatible
except ValueError as e:
        print(e)

#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".

c = b.transpose((1, 2, 0))

#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?

d = a + c # shapes match

#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.

print(a)
print(d)

# a + 1 = d (elementwise)

#12. Multiply a and c. Assign the result to e.

e = a*c
print(e)

#13. Does e equal to a? Why or why not?

# Yes, they're equal. Multyplication was done elementwise

#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"

d_max = d.max()
d_min = d.min()
d_mean = d.mean()

#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.

f = np.empty_like(d)

"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""

def classify(pos, properties, ndarray):
        maximum, minimum, avg = properties
        i, j, k = pos
        x = ndarray[i, j, k] 
        if x == minimum:
                return 0
        if x == avg:
                return 50
        if x == maximum:
                return 100
        if x < avg:
                return 25
        if x > avg:
                return 75

properties = (d_max, d_min, d_mean)

for i in range(d.shape[0]):
        for j in range(d.shape[1]):
                for k in range(d.shape[2]):
                        pos = (i, j, k)
                        f[i, j, k] = classify(pos, properties, d)

# seguro que hay alguna manera mas facil de hacerlo... f = np.map(classify, d)?

#17. Print d and f. Do you have your expected f?

print(d)
print(f)

"""
#18. Bonus question: instead of using numbers (i.e. 0, 25, 50, 75, and 100), how to use string values 
("A", "B", "C", "D", and "E") to label the array elements? You are expecting the result to be:
array([[[ 'D',  'D',  'D',  'B',  'D'],
        [ 'D',  'D',  'B',  'B',  'B'],
        [ 'D',  'B',  'D',  'D',  'D']],

       [[ 'B',  'B',  'B',  'B',  'E'],
        [ 'D',  'D',  'D',  'D',  'D'],
        [ 'B',  'D',   'A',  'D', 'D']]])
Again, you don't need Numpy in this question.
"""
f = np.empty_like(d, dtype="object")

def classify_letters(pos, properties, ndarray):
        maximum, minimum, avg = properties
        i, j, k = pos
        x = ndarray[i, j, k] 
        if x == minimum:
                return "E"
        if x == avg:
                return "C"
        if x == maximum:
                return "A"
        if x < avg:
                return "D"
        if x > avg:
                return "B"

for i in range(d.shape[0]):
        for j in range(d.shape[1]):
                for k in range(d.shape[2]):
                        pos = (i, j, k)
                        f[i, j, k] = classify_letters(pos, properties, d)

print(f)