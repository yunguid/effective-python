"""
imagine we wanted to sort a list of numbers but prioritize one group of numbers to
come first.

this pattern is useful when you're rendering a user interface and want important
messages or exceptional events to be displayed before everything else

A common way to do this is to pass a helper function as the key argument to a list's sort
method. the helper's return value will be used as the value for sorting each item in the list
The helper can check whether the given item is in the important gropu and can vary the sorting
value accordingly
"""


def sort_priority(values, group):
    def helper(x):
        if x in group:
            return (0, x)
        return (1, x)

    values.sort(key=helper)


numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 5, 7}
sort_priority(numbers, group)
print(numbers)


"""
3 reasons why this functions as expected:
    1. python supports closures, that is functions that refer to vars
    from the scope in which they were defined. This is why the helper function
    is able to access the group argument for sort_priority
    2. Functions are first-class objects in Python, meaning you can refer to them
    directly, assign them to variables, pass them as arguments to other functions, compare
    them in expressions and if statements and so on. This is how the sort method can accept a
    closure function as the key argument
    3. Python has specific rules for comparing sequences. It first compares item at index zero;
    then if those are equal it compares items at index one; etc........so on and sooooooooo on

It'd be nicer asf if this function returned whether higher-priority items were seen at all so the user
interface code can acta accordingly. Adding such behavior seems straightforward.
"""


def sort_priority_2(numbers, group):
    found = False

    def helper(x):
        if x in group:
            found = True
            return (0, x)
        return (1, x)

    numbers.sort(key=helper)
    return found


found = sort_priority_2(numbers, group)
print("found:", found)
print(numbers)

"""
WAIT but how the HELL is found false?
This is because when you reference a variable in an expression, the Python interpreter traverses
the scope to resolve the reference in this order

1. Current function's scope
2. Any enclosing scopes (such as other containing functions)
3. the scope of the module that contains the code (also called the global scope)
4. the built-in scope (that contains functions like len and str)

The found variable is assigned to True in the helper closure

In Python, there is special syntax for getting data out of a closure. The nonlocal statement
is used to indicate that scope traversal should happen upon assignment for a specific variable name
The only limit is that nonlocal won't traverse up to the module level scope
"""


def sort_priority_3(numbers, group):
    found = False

    def helper(x):
        nonlocal found
        if x in group:
            found = True
            return (0, x)
        return (1, x)

    numbers.sort(key=helper)
    return found


found = sort_priority_3(numbers, group)
print("found:", found)
print(numbers)


"""
nonlocal is good but becareful about over doing it.
"""


class Sorter:
    def __init__(self, group):
        self.group = group
        self.found = False

    def __call__(self, x):
        if x in self.group:
            self.found = True
            return (0, x)
        return (1, x)


sorter = Sorter(group)
numbers.sort(key=sorter)
assert sorter.found is True
