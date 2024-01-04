"""   بِسْمِ اللهِ الرَّحْمٰنِ الرَّحِيْمِ   """
 #==->  Md Sumon Hossain Khan <-==#  

"""
Python Numbers
There are three numeric types in Python:
1. int
2. float
3. complex
Variables of numeric types are created when you assign a value to them.

Example:
x = 1    # int
y = 2.8  # float
z = 1j   # complex

"""

"""
Type Conversion::>
You can convert from one type to another with the int(), float(), and complex() methods.

"""

#Example: Convert from one type to another
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# Note: You cannot convert complex numbers into another number type.

"""
Random Number::>
Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers.

"""

# Example: Import the random module, and display a random number between 1 and 9.

import random

print(random.randrange(1, 10))

