"""   بِسْمِ اللهِ الرَّحْمٰنِ الرَّحِيْمِ   """
 #==->  Md Sumon Hossain Khan <-==#  

# Variables::==-> Variables are containers for storing data values.
"""
Creating Variaables::>
1. Python has no command for declaring a variable.
2. A variable is created the moment you first assign a value to it.

"""
# Example:
x = 5
y = "Sumon"
print(x) 
print(y)

"""
Variables do not need to be declared with any particular type, and can even change type after they have been set.
"""
#Example: 
x = 4       # x is of type int
x = "Sumon" # x is now of type str
print(x)    # Output: Sumon

"""
Casting::>
If you want to specify the data type of a variable, this can be done with casting.
"""
#Example:
x = str(3)
y = int(3)
z = float(3)

print(x)  # Output: x will be '3'  
print(y)  # Output: will be 3
print(z)  # Output: will be 3.0

"""
Get The Type::>
You can get the data type of a variable with the type() function.
"""
#Example:
x = 5      # Output: <class 'int'>
y = "Sumon" # Output: <class 'str'>

print(type(x))    
print(type(y))  

"""
Single or Double Quotes?
=>String variables can be declared either by using single or double quotes.
"""
#Example:
x = "Sumon"
print(x)
#double quotes are the same as single quotes:
x = 'Sumon'
print(x)

"""
Case-Sensitive::>
Variable names are case-sensitive.
"""
#Example: This will create two variables.
a = 4
A = "Sumon"
# A will not overwrite a.
print(a)  # Output: 4
print(A)  # Output: Sumon