"""
Handling missing keys. There are a variety of ways to do this

For example, say I want to keep track of cities that I've visited in countries around the world
Here we have a dictionary that maps country names to a set instance containing corresponding city names
"""

visits = {
    "Mexico": {"Tulum", "Puerto Vallarta"},
    "Japan": {"Hakone"},
}
"""
we can use the set default method to add new cities to the sets, whether the country
name is already present in the dictionary or not.

This approach is shorter than achieving the same behavior with the get method and
an assignment expression
"""
# short
visits.setdefault("France", set()).add("Arles")
# long
if (japan := visits.get("Japan")) is None:
    visits["Japan"] = japan = set()
japan.add("Kyoto")

print(visits)


"""
What is you do control creation of the dictionary being accessed?
Case when you're using a dictionary instance to keep track of the internal state of a class

Here we wrap the example above in a class with helper methods to access the dynamic
inner state stored in a dict
"""


class Visits:
    def __init__(self):
        self.data = {}

    def add(self, country, city):
        city_set = self.data.setdefault(country, set())
        city_set.add(city)


"""
This new class hides the complexity of calling setdefault correctly and
provides a nicer interface for the programmer
"""
visits = Visits()
visits.add("Russia", "Yekaterinburg")
visits.add("Tanzania", "Zanzibar")
print(visits.data)


"""
This implementation of Visits.add is not ideal.
The setdefault method is confusingly named, and it constructs a new set instance on
every call, regardless of whether the given country was alreayd present in the data
dictionary

This is where 'defaultdict' from collections comes in handy. It automatically stores a
default value when a key doesn't exist.
"""
from collections import defaultdict


class Visits:
    def __init__(self):
        self.data = defaultdict(set)

    def add(self, country, city):
        self.data[country].add(city)


visits = Visits()
visits.add("England", "Bath")
visits.add("England", "London")
print(visits.data)

"""
TTR:
    1. If you're creating a dictionary to manage an arbitrary set of potential keys,
       then you should prefer using a defaultdict instance from the collections built-in module.
       This is because defaultdict takes care of providing default values for missing keys,
       which simplifies your code and prevents bugs related to missing keys or unnecessary allocations.
    2. If a dictionary of arbitrary keys is passed to you, and you don't control its creation,
       then you should prefer the get method to access its items.
       This approach avoids side effects like inserting new keys and is safer if you don't know the dictionary's exact type or behavior.

       get(key, default) does NOT modify the dictionary if the key is missing. It will just
       return the default value
       setdefault(key, default) will modify the dictionary if the key is missing
"""
