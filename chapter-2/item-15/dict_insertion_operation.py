"""
Starting in version 3.6 and officially in 3.7, dictionaries preserver insertion ordering.
This was NOT the case before.
"""

baby_names = {
    "cat": "kitten",
    "dog": "puppy",
}
print(baby_names)
print(list(baby_names.keys()))
print(list(baby_names.values()))
print(baby_names.popitem())
"""
Key word arguments to functions (**kwargs) used to come through in seemingly
random order before this change
"""


def my_func(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


my_func(goose="gosling", kangaroo="joey")


"""
Classes also use the dict type for their instance dictionaries

In previous versions of Python, object fields would show randomizing behavior
"""


class MyClass:
    def __init__(self):
        self.alligator = "hatchling"
        self.elephant = "calf"


a = MyClass()
for key, value in a.__dict__.items():
    print("%s = %s" % (key, value))


"""
Python is not statically types, so most code relies on duck typing, where an object's behavior is its
type
"""

votes = {
    "otter": 1281,
    "polar bear": 587,
    "fox": 863,
}


def populate_ranks(votes, ranks):
    names = list(votes.keys())
    names.sort(key=votes.get, reverse=True)
    for i, name in enumerate(names, 1):
        ranks[name] = i


def get_winner(ranks):
    return next(iter(ranks))


ranks = {}
populate_ranks(votes, ranks)
print(ranks)
winner = get_winner(ranks)
print(winner)

from collections.abc import MutableMapping


class SortedDict(MutableMapping):
    def __init__(self):
        self._data = {}

    def __getitem__(self, key):
        return self._data[key]

    def __setitem__(self, key, value):
        self._data[key] = value

    def __delitem__(self, key):
        del self._data[key]

    def __iter__(self):
        keys = list(self._data.keys())
        keys.sort()
        for key in keys:
            yield key

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return repr(self._data)


ranks = SortedDict()
populate_ranks(votes, ranks)
print(ranks)
