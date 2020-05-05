"""
Python exposes a terse and intuitive syntax for performing 
slicing on lists and strings. This makes it easy to reference
only a portion of a list or string. 

This Stack Overflow answer provides a brief but thorough
overview: https://stackoverflow.com/a/509295

Use Python's slice syntax to achieve the following:
"""

a = [2, 4, 1, 7, 9, 6]

# Output the second element: 4:
slice = a[1:2]
print(slice)

# Output the second-to-last element: 9
slice = a[4:-1]
print(slice)

# Output the last three elements in the array: [7, 9, 6]
slice =a [3:]
print(slice)

# Output the two middle elements in the array: [1, 7]
slice =a [2:-2]
print(slice)

# Output every element except the first one: [4, 1, 7, 9, 6]
slice =a [1:]
print(slice)

# Output every element except the last one: [2, 4, 1, 7, 9]
slice = a[0:-1]
print(slice)

# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"
part = s [7:12]
print(part)