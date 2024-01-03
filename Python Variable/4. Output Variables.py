"""   بِسْمِ اللهِ الرَّحْمٰنِ الرَّحِيْمِ   """
 #==->  Md Sumon Hossain Khan <-==#  

"""
Output Variables::>
The Python print() function is often used to output variables.

"""
#Example:
x = "Python World"
print(x)

# In the print() function, you output multiple variables, separated by a comma:
x = "Sumon"
y = "Python"
z = "World"
print(x, y, z)

# You can also use the '+' operator to output multiple variables:
x = "Sumon "
y = "Python "
z = "World"
print(x + y + z)

""" Notice the space character after "Python " and "is ", without them the result would be "Pythonisawesome". """

# For numbers, the '+' character works as a mathematical operator:
x = 5
y = 10
print(x + y)

"""
In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:

Example: TypeError: unsupported operand type(s) for +: 'int' and 'str'
x = 5
y = "Musafir"
print(x + y)

"""

"""
The best way to output multiple variables in the print() function is to separate them with commas,
which even support different data types:

"""
#Example: 
x = 5
y = "Musafir"
print(x, y)