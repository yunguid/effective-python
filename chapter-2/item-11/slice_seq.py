"""
Many programs are used to automate repetitive tasks that are better suited to machines
Lists and dict types are can be used to solve a variety of problems.
Python has special syntax and built in modules that enhance readability and extend
the capabilities of lists and dictionaries beyond simple array, vector, and hash table
types

Slicing sequences:
- Slicing allows you to access a subset of a sequence of items with minimal effort
  and can be extended to any Python class that implements __getitem__ and __setitem___
  specia methods
- basic syntax is: somelist[start:end] where START is INCLUSIVE and END is EXCLUSIVE
"""

a = ["a", "b", "c", "d", "e", "f", "g", "h"]
print("Middle two:   ", a[3:5])
print("All but ends: ", a[1:7])


# when slicing from the start of a list, leave out the zero index to reduce visual noise
assert a[:5] == a[0:5]
print(a[:5])

assert a[5:] == a[5 : len(a)]  # len(a) will return 8
print(len(a))
print(f"a[5:]: {a[5:]} a[5:len(a)]: {a[5 : len(a)]}")

a[:]  # ["a", "b", "c", "d", "e", "f", "g", "h"]
a[:5]  # ["a", "b", "c", "d", "e"]
a[:-1]  # ["a", "b", "c", "d", "e", "f", "g"]
a[4:]  # ["e", "f", "g", "h"]
a[-4:]  # ^ same
a[-3:]  # ['f', 'g', 'h']
a[-4:-1]  # e, f, g
a[-3:-1]

b = a[3:]
print("Before:   ", b)
b[1] = 99
print("After:   ", b)
print("no change", a)


print("Before", a)
a[2:7] = [99, 22, 14]

print("After    ", a)

print("Before   ", a)
a[2:3] = [23423, 12]
print("After    ", a)


b = a[:]
assert b == a and b is not a

"""
if you assign to a slice with no start or end indexes, you replace the entire contents
of the list with a copy of what's reference (instead of allocating a new list)
"""
b = a
print("before a", a)
print("before b", b)
a[:] = [101, 102, 103]
assert a is b
print("after a  ", a)
print("after b  ", b)

"""
- avoid being verbose when slicing, don't supply 0 for the start of the lenght of the
sequence for the end index
"""
