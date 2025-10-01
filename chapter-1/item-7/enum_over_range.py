"""
Prefer enum over range
"""

# The range built-in function is useful for loops that iterate over a set of integers
from random import randint

random_bits = 0
for i in range(3):
    if randint(0, 1):
        """
        << i means shift left by 'i' positions
       1 << 0 -> 0b..0001(still 1)
       1 << 1 -> 0b..0010(decimal 2)
       1 << 2 -> 0b..0100(decimal 4)
       1 << 5 -> 0b..100000(decimal 32)
        """
        random_bits |= 1 << i
    print(bin(random_bits))


# when you have a data structure ot iterate over, like a list of strinsg,
# you can loop directly over the sequence
flavor_list = ["vanilla", "chocolate", "pecan", "strawberry"]
for flavor in flavor_list:
    print(f"{flavor} is delicious")

# often you will want to loop over a list and know the index of the current
# Let's say you wanted to print rankings
for i in range(len(flavor_list)):
    flavor = flavor_list[i]
    print(f"{i + 1}: {flavor}")
# this sucks balls cuz you hve to index into the array
# use enumerate; it wraps any iterator with a lazy generator

"""
A generator is a way to create an object taht produces a sequence of values lazily
instead of building the whole list in memory up front
"""
# non-generator
nums = [x * x for x in range(5)]
print(nums)

# generator
nums = (x * x for x in range(5))
print(nums)
# you can pull values one at a time:
print(next(nums))

# enumerate yields pairs of the loop index and the next value from the given
# iterator
it = enumerate(flavor_list)
print(it)
print(next(it))
print(next(it))

for i, flavor in enumerate(flavor_list):
    print(f"{i + 1}: {flavor}")

# can make it even shorter
for i, flavor in enumerate(flavor_list, 1):
    print(f"{i}: {flavor}")

"""
`enumerate` provides concise syntax for looping over an iterator and getting the index
of each item from the iterator as you go
"""
