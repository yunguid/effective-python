"""
In python you may pass arguments by position when
calling a function
"""


def remainder(number, divisor):
    return number % divisor


assert remainder(20, 7) == 6

"""
All normal args to python functions can also be passed in by keyword, where
the name of the argument is used in an assignment within the parentheses of
a func call. Can be passed in any order as long as all
of the required positional args are specified
"""
remainder(20, 7)
remainder(20, divisor=7)
remainder(number=20, divisor=7)
remainder(divisor=7, number=20)

# positional args must be specified before keyword args
# remainder(number=20,7)

"""
if you already have a dictionary and want to use its contents to call
a function like remainder, you can do this by using the ** operator

This instructs python to pass the values from the dictionary as the corresponding
keyword arguments of the function
"""
my_kwargs = {
    "number": 20,
    "divisor": 7,
}

assert remainder(**my_kwargs) == 6


"""
You can mix the ** operator with positional arguments or keyword
arguments in the function call as long as no argument is repeated
"""
my_kwargs = {
    "divisor": 8,
}
assert remainder(number=20, **my_kwargs) == 4


"""
You can also use the ** operator multiple times if you know that the dictionaries
don't contain overlapping keys
"""

my_kwargs = {
    "number": 20,
}
other_kwargs = {
    "divisor": 7,
}
assert remainder(**my_kwargs, **other_kwargs) == 6

"""
if you'd like for a function to receive any named keyword argument, you
can use the **kwargs catch-all parameter to collect those
arguments into a dict that you can process
"""


def print_parameters(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")


print_parameters(dog="golden retriever", captain="kraiklyn", food="banana")


"""
The flexibility of keyword arguments provides 3 significant benefits:
    1. key word args make the function call clearer to new readers of the code
        - with the call remainder(20,7) it's not evident which argument is
        number and which is divisor unless you look at the implementation.
        In the call with the keyword args, it is immediately obvious
    2. they can have default values specified in the function definition. this
       allows a function to provide additional capabilities when you need them, but
       you can accept the default behavior most of the time.
"""


def flow_rate(weight_diff, time_diff):
    return weight_diff / time_diff


weight_diff = 0.5
time_diff = 3
flow = flow_rate(weight_diff, time_diff)
print(f"{flow:.3} kg per second")


"""
add time period scaling factor
"""


def flow_rate(weight_diff, time_diff, period):
    return (weight_diff / time_diff) * period


"""
Problem now is that I need to specify the period argument every time
I call the function even in the common case of flow rate per second

We can give period a default value
"""


def flow_rate(weight_diff, time_diff, period=1):
    return (weight_diff / time_diff) * period


flow_per_second = flow_rate(weight_diff, time_diff)
flow_per_hour = flow_rate(weight_diff, time_diff, period=3600)

"""
Third reason to use keyword arguments is that they provide a powerful
way to extend a function's parameters while remaining backward compatible with
existing callers.

For example, say I want to extend the flow_rate function above to calculate
flow rates in weight units besides kilograms
"""


def flow_rate(weight_diff, time_diff, period=1, units_per_kg=1):
    return ((weight_diff * units_per_kg) / time_diff) * period


pounds_per_hour = flow_rate(weight_diff, time_diff, period=3600, units_per_kg=2.2)
print(pounds_per_hour)

"""
TTR:
    1. function arguments can be specified by position or by keyword
    2. keywords make it clear what the purpose of each argument is when it would be
    confusing
    3. keyword arguments with default values make it easy to add new behaviors to a
   function without needing to migrate all existing callers
   4. optional keyword arguments should always be passed by keyword instead of by position
"""
