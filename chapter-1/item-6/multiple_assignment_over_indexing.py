"""
Python has a built in tuple type that can be used to create immutable
ordered sequences of values
"""

import time

snack_cals = {
    "chips": 140,
    "popcorn": 80,
    "nuts": 190,
}
items = tuple(snack_cals.items())
print(items)

# the values in tuples can be accessed through numerical indices
item = ("Peanut butter", "jelly")
first = item[0]
second = item[1]
print(first, "and", second)

# once a tuple is created, you can't modify it by assigning a new val to an index
try:
    pair = ("chocolate", "peanut butter")
    pair[0] = "honey"
except Exception as e:
    print(e)
# Python also has syntax for unpacking
# this allows for assigning multiple values in a single statement
item = ("peanut butter", "jelly")
first, second = item
print(first, "and", second)
# this requires less lines than indexing


favorite_snacks = {
    "salty": ("doritos", 200),
    "sweet": ("swedish fish", 300),
    "veggie": ("carrots", 30),
}
((type1, (name1, cals1)), (type2, (name2, cals2)), (type3, (name3, cals3))) = (
    favorite_snacks.items()
)
print(f"favorite {type1} is {name1} with {cals1} calories")
print(f"favorite {type2} is {name2} with {cals2} calories")
print(f"favorite {type3} is {name3} with {cals3} calories")


def bubble_sort(a):
    for _ in range(len(a)):
        for i in range(1, len(a)):
            if a[i] < a[i - 1]:
                temp = a[i]
                a[i] = a[i - 1]
                a[i - 1] = temp


names = ["abraham", "cain", "abel", "judah", "luke"]
print(len(names))
start = time.time()
bubble_sort(names)
end = time.time()
print(f"Names: {names}, Time elapsed: {end - start}")


# With unpacking syntax, we can swap indexes in a single line
def bubble_sort(a):
    for _ in range(len(a)):
        for i in range(1, len(a)):
            if a[i] < a[i - 1]:
                a[i - 1], a[i] = a[i], a[i - 1]


names = ["abraham", "cain", "abel", "judah", "luke"]
print(len(names))
start = time.time()
bubble_sort(names)
end = time.time()
print(f"Names: {names}, Time elapsed: {end - start}")

"""
The right side of the assignment (a[i], a[i-1]) is evaluated first, and its values are
put into a new temporary tuple
Then the left side is used to receive that tuple value and assign it to the variable names a[i-1] and a[i]
"""

snacks = [("bacon", 350), ("donut", 240), ("muffin", 190)]
for i in range(len(snacks)):
    item = snacks[i]
    name = item[0]
    calories = item[1]
    print(f"#{i + 1}: {name} has {calories} calories")

# above works but is noisy. too many extra chars required to index into the various levels
# here we use enumerate instead
for rank, (name, calories) in enumerate(snacks, 1):
    print(f"#{rank}: {name} has {calories} calories")


"""
Python has special syntax called unpacking for assigning multiple values in a single statement

Unpacking is generalized in Python and can be applied to any iterable

reduce visual noise and increase code clarity by using unpacking to avoid explicitly indexing into
sequences
"""
