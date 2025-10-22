"""
Accepting a varaible number of positional arguments can make a function call clearer
and reduce visual noise. These positional arguments are often called varargs for short
or star args

for example, say that I want ot log some debugging information. With a fixed
number of arguments, I would need a function that takes a message and list of
values
"""


def log(message, values):
    if not values:
        print(message)
    else:
        values_str = ", ".join(str(x) for x in values)
        print(f"{message}: {values_str}")


log("my numbers are ", [2, 3, 4, 5])
log("Luke, I am your Father", [])

"""
having to pass an empty list when I have no values to log is cumbersome and noisy.
It'd be much better to leave out the second argument entirely.
We can do this in Python by prefixing the last positional parameter name with *.
"""


def log(message, *values):
    if not values:
        print(message)
    else:
        values_str = ", ".join(str(x) for x in values)
        print(f"{message}: {values_str}")


log("My number are", 1, 2)
log("Hi there")


favorites = [7, 33, 99]
log("Favorite colors", *favorites)


def my_generator():
    for i in range(10):
        yield i


def my_func(*args):
    print(args)


it = my_generator()
my_func(*it)

"""
Therea re two problems with accepting a varaible number of positional arguments
1. these optional positional arguments are always turned into a tuple before passed
   to a function. This means that if the caller of a function uses the * operator
   on a generator, it will be iterated until it's exhausted
2. You can't add new positional arugments ot a function in the futuer without migrating
    caller
"""


def log(sequence, message, *values):
    if not values:
        print(f"{sequence} - {message}")
    else:
        values_str = ", ".join(str(x) for x in values)
        print(f"{sequence} - {message}: {values_str}")


log(1, "favorites", 7, 33)
log(1, "hi there")
log("favorite nums", 7, 33)

"""
TTR:
    - functions can accept a variable number of positional arguments by using
        *args in the def statement
    - you can use the items from a sequence as the positional arguments for a
    function with the * operator
    - using the * operator with a generator may cause a program to run
    out of memory and crash
    - adding new positional parameters to functions that accept
    *args can introduce hard-to-detect bugs
"""
