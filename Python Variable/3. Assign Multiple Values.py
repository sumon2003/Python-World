"""   بِسْمِ اللهِ الرَّحْمٰنِ الرَّحِيْمِ   """
 #==->  Md Sumon Hossain Khan <-==#  

"""

Many Values to Multiple Variables::>
Python allows you to assign values to multiple variables in one line.

"""
#Example: 
x, y, z = "Soil", "Water", "Air"
print(x)
print(y)
print(z)

# Note: Make sure the number of variables matches the number of values, or else you will get an error.

"""

One Value to Multiple Variables::>
And you can assign the same value to multiple variables in one line.

"""
#Example:
x = y = z = "Water"
print(x)
print(y)
print(z)

"""

Unpack a Collection::>
If you have a collection of values in a list, tuple etc.
Python allows you to extract the values into variables. 
This is called unpacking.

"""

# Example: Unpack a list =>

Element = ["Soil", "Water", "Air"]
x, y, z = Element

print(x)  # Output:  Soil
print(y)  # Output:  Water
print(z)  # Output:  Air
