"""   بِسْمِ اللهِ الرَّحْمٰنِ الرَّحِيْمِ   """
 #==->  Md Sumon Hossain Khan <-==#  

"""
Global Variables::>
Variables that are created outside of a function (as in all of the examples above) are known as global variables.

Global variables can be used by everyone, both inside of functions and outside.

"""
#Example: Create a variable outside of a function, and use it inside the function
x = "World"
def myfunc():
    print("Python " + x)

myfunc()    

"""
If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. 
The global variable with the same name will remain as it was, global and with the original value.

"""
#Example: Create a variable inside a function, with the same name as the global variable
x = "World"
def myfunc():
    x = "Snake"
    print("Python " + x)  # Output: Python Snake

myfunc()

print("Python " + x)      # Output: Python World

"""
The global Keyword::>
Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

To create a global variable inside a function, you can use the 'global' keyword.

"""
# Example: If you use the 'global' keyword, the variable belongs to the global scope
def myfunc():
    global x
    x = "World"

myfunc()

print("Python " + x)   # Output: Python World

"""
Also, use the 'global' keyword if you want to change a global variable inside a function.

Example:
To change the value of a global variable inside a function, refer to the variable by using the global keyword:
"""
x = "World"
def myfunc():
    global x
    x = "Snake"

myfunc()

print("Python " + x)   # Output: Python Snake