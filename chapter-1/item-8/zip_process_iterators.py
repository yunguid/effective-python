"""
Use zip to process iterators in Paralell:
    - You may find yourself often with many lists of related objects
    - List comprehensions make it easy to take a source list and get a derived
    list by applying an expression
"""

names = ["cecilia", "lise", "marie"]
counts = [len(n) for n in names]
print(counts)

# The items in the derived list are related to the items in the
# source list by their indices.
# We can iterate over both lists in parallel.
longest_name = None
max_count = 0

for i in range(len(names)):
    count = counts[i]
    if count > max_count:
        longest_name = names[i]
        max_count = count
print(longest_name)

# above is too noisy
# using enumerate helps, but is still not ideal
for i, name in enumerate(names):
    count = counts[i]
    if count > max_count:
        max_count = count
        longest_name = name
print(longest_name)

"""
Zip is another built-in function. It wraps two or more iterators with a lazy
generator. The zip generator yields tuples containing the next value from each
iterator. Can be unpacked in for loop
"""
for name, count in zip(names, counts):
    if count > max_count:
        longest_name = name
        max_count = count
print(longest_name)

names.append("caroline")
for name, count in zip(names, counts):
    print(name)  # caroline not in there because tuples are different lengths
"""
Zip yields tuples until any one of the wrapped iterators is exhausted.
Its output is as long as its shortest input
"""
matrix = [[1, 2, 3], [4, 5, 6]]
transposed = list(zip(*matrix))
print(transposed)

# # this is what the * is doing
# def f(a, b, c):
#     print(a, b, c)

# args = [1, 2, 3]
# f(*args)

import itertools

for name, count in itertools.zip_longest(names, counts):
    print(f"{name}: {count}")


"""
- zip can be used to iterator over multiple iterators in parallel
- zip creates a lazy generator that producers tuples
- zip truncates its output silently to the shortest iterator if you supply it
  with iterators of different lengths
- use zip_longest from itertools as a solution
"""
