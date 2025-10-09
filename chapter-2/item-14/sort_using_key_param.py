"""
the 'list' built-in type provides a 'sort' method for ordering the items in a list
instance based on a variety of criteria.

'sort' will order a list's contents by the natural ascending order of the items
"""

numbers = [93, 86, 11, 68, 70]
numbers.sort()
print(numbers)


"""
sort method works for nearly all built-in types (strings, floats, etc..) that
have a natural odering to htem.

What does 'sort' do with objects? Example:
"""


class Tool:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __repr__(self):
        return f"Tool({self.name!r}, {self.weight})"


tools = [
    Tool("level", 3.5),
    Tool("hammer", 1.25),
    Tool("screwdriver", 0.5),
    Tool("chisel", 0.25),
]

"""

 tools.sort() does not work here because the 'sort' method tries to call
 comparison special methods that are not defiend by the class

To support this use case, the sort method accepts a key parameter that's expected
to be a function.

The key function is passed a single argument, which is an item from the list
that is being sorted

The return value of the key function should be a comparable value to use
in place of an item for sorting purposes
"""

print("unsorted:", repr(tools))
tools.sort(key=lambda x: x.weight)
print("\nSorted:    ", tools)

"""
When you call
something.sort(key=fn)
Python sorts the list by the value that comes out of calling fn(item) for each
item in the list
"""
# sort by length of strings
names = ["Luke", "Charles", "Harry", "Garrett", "Elon", "David"]
names.sort()
print(names)
names.sort(key=len)
print(names)


# sort numbers by their absoluate value
nums = [-10, 5, -3, 8, 1]
nums.sort(key=abs)
print(nums)


# sort a list of tuples by the second element
pairs = [(2, 100), (1, 50), (4, 25), (2, 11)]
pairs.sort(key=lambda p: p[1])
print(pairs)

"""
Within the lambda function you can access attributes of items

For basic types like strings, you may even want to use the key function to do
transformations on the values before sorting
"""
places = ["home", "work", "New York", "Paris"]
places.sort()
print("Case sensitive:  ", places)
places.sort(key=lambda x: x.lower())
print("Case insensitive:", places)

# how can I sort first by weight and then by name?
power_tools = [
    Tool("drill", 4),
    Tool("circular saw", 5),
    Tool("jackhammer", 40),
    Tool("sander", 4),
]

"""
The simplest solution is to use the tuple type. Tuples are immutable sequences of
arbitrary Python values. Tuples are comparable by default and have a natural ordering
meaning thath they implement all of the special methods such as __lt__, that are required
by the sort method. l

Tuples implement these special method comparators by iterating over each position
in the tuple and comparing the corresponding values one index at a time.
"""
saw = (5, "circular saw")
jackhammer = (40, "jackhammer")
assert not (jackhammer < saw)

# if the first position in the tuples being compared are equal, weight in this case,
# then the tuple comparison will move on to the second position and so on
drill = (4, "drill")
sander = (4, "sandrrrrrr")
assert drill[0] == sander[0]
assert drill[1] < sander[1]
assert drill < sander

power_tools.sort(key=lambda x: (x.weight, x.name))
print(power_tools)

power_tools.sort(key=lambda x: (x.weight, x.name), reverse=True)
print(f"Descending: {power_tools}")


class Purchase:
    def __init__(self, description, cost):
        self.description = description
        self.cost = cost

    def __repr__(self):
        return f"Purchase ({self.description!r}, {self.cost})"


purchases = [
    Purchase("uber", 1000),
    Purchase("clothes", 200),
    Purchase("ai", 10000),
    Purchase("gim", 200),
]

purchases.sort(key=lambda x: x.description)
print(f"Sorted by name, alphabetically, ascending: {purchases}")

purchases.sort(key=lambda x: x.cost)
print(purchases)

purchases.sort(key=lambda x: (x.description, x.cost), reverse=True)
print(purchases)
