"""
3 fundamental operations for interating with dictionaries:
    1. Accessing
    2. Assigning
    3. Deleting keys and associated values

The contents of dictionaries are dynamic and it is possible that when you try to access
or delete a key it won't already be present
"""

counters = {
    "pumpernickel": 2,
    "sourdough": 1,
}
"""
To increment the counter for a new vote, we need to check if the key exists,
insert the key with a default counter value of zero if it's missing, and
then increment the counter's value. This requires accessing the key two times
and assigning it once
"""
key = "wheat"
if key in counters:
    count = counters[key]
else:
    count = 0
counters[key] = count + 1

"""
Another way to accomplish the same behavior is by relying on how dictionaries raise a
KeyError exception when you try to get the value for a key that doesn't exist. This
is more efficient as it requires only one access and one assignment
"""
try:
    count = counters[key]
except KeyError:
    count = 0
counters[key] = count + 1

"""
This flow of fetching a key that exists or returning a default value is so common
that the dict built-in type provides the get method to accomplish this task

The second parameter to 'get' is the default value to return in the case that the
key is not present. This requires one access and one assignment, but is shorter than
the above method
"""
count = counters.get(key, 0)
counters[key] = count + 1


"""
What if the values of the dictionary are a more complex type, like a list?
For example, say that instead of only counting votes, we also want to know who voted
for each type of bread.

Here we do this by associating a list of names with each key
"""
votes = {
    "baguette": ["Bob", "Alice"],
    "ciabatta": ["Coco", "Deb"],
}
key = "brioche"
who = "Elmer"

if key in votes:
    names = votes[key]
else:
    votes[key] = names = []

names.append(who)
print(votes)

"""
Relying on the 'in' expression requires two accesses if the key is present, or one
access and one assignment if the key is missing
"""

try:
    names = votes[key]
except KeyError:
    votes[key] = names = []
names.append(who)
# get method
names = votes.get(key)
if names is None:
    votes[key] = names = []
names.append(who)

"""
This approach involves using get to fetch list values can be shortened by
one line if you use an assignment expression in the 'if' statement, which
improves readability
"""
if (names := votes.get(key)) is None:
    votes[key] = names = []
names.append(who)

"""
The 'dict' type also provides 'setdefault' method to help shorten this pattern even further.
'setdefault' tries to fetch the value of a key in the dictionary.
if the key is not present, the method assigns that key to the default value provided
then the method returns the value for that key

This is not prefered because the naming is confusing. Why called set when it is
actually getting the value for that key
"""
names = votes.setdefault(key, [])
names.append(who)

"""
Another important thing to note about 'setdefault' is that the default value
passed to the this method is assigned directly into the dictionary when the key is
missing instead of being copied
"""

data = {}
key = "foo"
value = []
data.setdefault(key, value)
print("before:", data)
value.append("hello luke")
print("after: ", data)

"""
this means that i need to make sure that i'm always constructing a new default value for
each key I access with setdefault. this leads to a significatn performance overhead in this
example because I have to allocate a list instance for each call.
"""

count = counters.setdefault(key, 0)
counters[key] = count + 1

"""
the problem here is that the call to setdefault is superfluous as you always need to assign
the key in the dictionary to a new value after you increment the counter, so the extra
assignment done by setdefault is unnecessary. The earlier approach using get for counter
updates requires only one access and one assignment, where this requires two assignments and
one access

instances to use setdefault:
    - when the default values are cheap to construct, mutable, there's no potential
    for raising exceptions

Things to Remember:
    1. there are four common ways to detect and handle missing keys in dictionaries:
        using 'in' expressions, 'KeyError' exceptions, the 'get' method, and the
        'setdefault' method
    2. 'get' method is best for dictionaries that contain basic types like counters
    3. when the setdefault method of dict seems like the best fit for your problem consider
    using the defaultdict instead.
"""

from collections import defaultdict

regular_dict = {}
regular_dict.setdefault("key1", []).append("item1")
regular_dict.setdefault("key2", []).append("item2")

# using defaultdict instead
auto_list_dict = defaultdict(list)
auto_list_dict["key1"].append("item1")
auto_list_dict["key2"].append("item2")

print(auto_list_dict)
from pprint import pprint

pprint(auto_list_dict)

for key, value in auto_list_dict.items():
    print(f"{key}: {value}")

print(regular_dict.keys())
print(regular_dict.values())
