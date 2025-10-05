"""
An assignment expression AKA the 'walrus operator' is a new syntax
introduced in Python 3.8 to solve a long standing problem with language that can cause
code duplication.
Normal assignment statements: a = b
Walrus assignment statements: a:=b

these are useful because they allow assignment of variables in places where these
assignment statements are disallowed, such in the conditional expression
of an if statement

Python EVALUATES assignments from right to left but BINDS names left to right
In the example below:
    - 5 is evaluated first, popped to the stack
    - Make a duplicate copy of the top of the stack, so there are two 5's
    - Pop the top 5 and assign it to 'a'
    - Make another duplicate
    - Assign to b
    - Assign to c
In C/C++ it is right-associative and nested as (a=(b=(c=5)))
Python treats assignments as a statement (not an expression)
"""

import dis


def f():
    a = b = c = 5
    return a, b, c


dis.dis(f)


fresh_fruit = {
    "apple": 10,
    "banana": 8,
    "lemon": 5,
}

"""
instead of doing:
"""


def make_lemonade(count): ...


def out_of_stock(): ...


count = fresh_fruit.get("lemon", 0)
if count:
    make_lemonade(count)
else:
    out_of_stock()

"""
we can do use the walrus operator
The assignment expression is first assigning a value to the count
variable, and then evaluating that value in the context of the if statement to
determine how to proceed
"""
if count := fresh_fruit.get("lemonade", 0):
    make_lemonade(count)
else:
    out_of_stock()


def make_cider(count): ...


count = fresh_fruit.get("apple", 0)
if count >= 4:
    make_cider(count)
else:
    out_of_stock()


if (count := fresh_fruit.get("apple", 0)) >= 4:
    make_cider(count)
else:
    out_of_stock()

"""
another common variation of this repetitive pattern occurs when I need to
assign a variable in the enclosing scope depending on some condition, and
then reference that variable shortly afterward in a function call
"""


def slice_bananas(count): ...


class OutOfBananas(Exception):
    pass


def make_smoothies(count): ...


pieces = 0

count = fresh_fruit.get("banana", 0)

if count >= 2:
    pieces = slice_bananas(count)
try:
    smoothies = make_smoothies(pieces)
except OutOfBananas:
    out_of_stock()

# other commons way to do this is to put the pieces = 0 assignment in the else block

count = fresh_fruit.get("banan", 0)
if count >= 2:
    pieces = slice_bananas(count)
else:
    pieces = 0

try:
    smoothies = make_smoothies(pieces)
except OutOfBananas:
    out_of_stock()

"""
Walrus operator can be used to shorten this example by one line of code. This small
change removes any emphasis on the count variable.
"""
pieces = 0
if (count := fresh_fruit.get("banana", 0)) >= 2:
    pieces = slice_bananas(count)

try:
    smoothies = make_smoothies(pieces)
except OutOfBananas:
    out_of_stock()


"""
switch / case statement type situation
"""
count = fresh_fruit.get("banana", 0)
if count >= 2:
    pieces = slice_bananas(count)
    to_enjoy = make_smoothies(pieces)
else:
    count = fresh_fruit.get("apple", 0)
    if count >= 4:
        to_enjoy = make_cider(count)
    else:
        count = fresh_fruit.get("lemon", 0)
        if count:
            to_enjoy = make_lemonade(count)
        else:
            to_enjoy = "nothing"

"""Walrus operatior provides an elegant solution for this"""
if (count := fresh_fruit.get("banana", 0)) >= 2:
    pieces = slice_bananas(count)
    to_enjoy = make_smoothies(pieces)
elif (count := fresh_fruit.get("apple", 0)) >= 4:
    to_enjoy = make_cider(count)
elif count := fresh_fruit.get("lemon", 0):
    to_enjoy = make_lemonade(count)
else:
    to_enjoy = "nothing"


"""
Another common frustration of new Python programmers is the lack of a do/while
loop construct.

In this example we bottle juice as new fruit is delivered until there's no fruit remaining
"""


def pick_fruit(): ...
def make_juice(count, fruit): ...


bottles = []
fresh_fruit = pick_fruit()
while fresh_fruit:
    for fruit, count in fresh_fruit.items():
        batch = make_juice(fruit, count)
        bottles.extend(batch)
    fresh_fruit = pick_fruit()

"""
This is repetitive because it requires two separate fresh_fruit=pick_fruit() calls
One before the loop to set initial conditions and another at the end of hte loop to
replenish the list of delivered fruit

A solution to improve this is called the loop-and-a-half idio. This eliminates
redundant lines, but also undermines the while loop's contribution by making it a dumb
infinite loop.
"""
bottles = []
while True:
    fresh_fruit = pick_fruit()
    if not fresh_fruit:
        break
    for fruit, count in fresh_fruit.items():
        batch = make_juice(fruit, count)
        bottles.extend(batch)

"""
the walrus operator obviates the need for the loop-and-a-half idiom by allowing the
fresh fruit var to be reassigned and then conditionally evaluated each time through
the while loop
"""
bottles = []
while fresh_fruit := pick_fruit():
    for fruit, count in fresh_fruit.items():
        batch = make_juice(fruit, count)
        bottles.extend(batch)
"""
- assignment expression use the walrus operator to both assign and evaluate variable
names in a single expression, thus reducing repetition
- when an assignment expression is a subexpression of a larger expression,  it must
be surrounded with parentheses
- although switch/case statements and do/while are not available in python, their
functionality can be emulated much more clearly by using assignment expressions
"""
