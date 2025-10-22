"""
___str___: Human readable description
- Nice for printing
- Used by print(obj) or str(obj)

__repr__: Developer/debug representation
- Unambiguous and technical
- Used by repr(obj) or when inspecting objects in REPL
"""


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f"{self.name} ({self.email})"

    def __repr__(self):
        return f"User(name={self.name!r}, email={self.email!r})"


name = "luke"
email = "luke@yng.sh"
user_1 = User(name, email)
print(str(user_1))
print(repr(user_1))


"""
Example: say I want a helper function that divides one number by another.
In the case of dividing by zero, returning None seems natural because the result is not defined
"""


def careful_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None


x, y = 1, 0
result = careful_divide(x, y)
if result is None:
    print("invalid inputs")

x, y = 0, 5
result = careful_divide(x, y)
if result is None:
    print(
        "invalid"
    )  # this runs but shouldn't since the result should be 0, not None which signals false

"""
Returning None from a function like this is error prone
Two ways to reduce such errors:
    1. split the return value into a two-tuple. first part of the tuple indicates that the operation
    was a success or failure. the second part is the actual result that was computed
"""


def careful_divide(a, b):
    try:
        return True, a / b
    except ZeroDivisionError:
        False, None


_, result = careful_divide(x, y)
if not result:
    print("invalid inputs")

"""
the better way is to never return None for special cases. Instead raise an Exception up to the caller
and have the caller deal with it.
"""


def careful_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError("invalid inputs")


x, y = 5, 2
try:
    result = careful_divide(x, y)
except ValueError:
    print("invalid inputs")
else:
    print("result is %.1f" % result)
