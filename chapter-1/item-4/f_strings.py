a = 0b10111011
b = 0xC5F
print(f"Binary is %d Hex is %d" % (a, b))

key = "my_var"
value = 1.234
try:
    formatted = "%-10s = %.2f" % (value, key)
    print(formatted)
except Exception as e:
    print(e)

pantry = [
    ("raisins", 1.25),
    ("bananas", 234234),
    ("cherries", 0.2),
]
for i, (item, count) in enumerate(pantry):
    print("#%d: %-10s = %.2f" % (i + 1, item.title(), round(count)))


# Problem with formatting expressions:
#   - If you want to use the same value in a format string multiple times,
#     you have to repeat in the right side tuple

template = "%s loves food. Let that retard %s cook!"
name = "Luke"
formatted = template % (name, name)
print(formatted)


name = "suzy"
formatted = template % (name.title(), name.title())
print(formatted)


# The % operator in Python has ability to do formatting witha dictionary instead of a
# tuple

key = "my_var"
value = 1.234

old_way = "%-10s = %.2f" % (key, value)
new_way = "%(key)-10s = %(value).2f" % {"key": key, "value": value}
reordered = "%(key)-10s = %(value).2f" % {"value": value, "key": key}

assert old_way == new_way == reordered

# Using dictionaries also allows mutliple format specifiers to reference the
# same value, thus making it unnecssary to supply that value more than once

name = "yunguid"
template = "%s loves food. see %s cook."
before = template % (name, name)
template = "%(name)s loves food. see %(name)s cook."
after = template % {"name": name}
assert before == after

# using dictionaries in formatting expressions increases verbosity

soup = "lentil"
formatted = "today's soup is %(soup)s." % {"soup": soup}
print(formatted)

# too long
menu = {
    "soup": "lentil",
    "oyster": "kumamoto",
    "special": "schnitzel",
}
template = (
    "Today's soup is %(soup)s, "
    "buy one get two %(oyster)s oysters, "
    "and our special entree is %(special)s"
)
formatted = template % menu
print(formatted)

# Python 3 added support for advanced string formatting that is more
# expressive than the old C-style format strings that use the % operator
# Accessed through the built in format function

a = 1234.5678
formatted = format(a, ",.2f")  # , does thousands separations
print(formatted)

b = "my string"
formatted = format(b, "^2s")  # ^ centers
print("*", formatted, "*")

# can specify placeholders with {}
key = "my_var"
value = 1.234

formatted = "{} = {}".format(key, value)
print(formatted)

formatted = "{:<10} = {:.2f}".format(key, value)
print(formatted)

print("%.2f%%" % 12.5)
print("{} replaces {{}}".format(1.23))

formatted = "{1} = {0}".format(key, value)
print(formatted)

formatted = "{0} loves food. See {0} cook.".format(name)
print(formatted)

# format does not address problem with code readability when you need to amke modifications
# to values before formatting them.
for i, (item, count) in enumerate(pantry):
    old_style = "#%d: %-10s = %d" % (i + 1, item.title(), round(count))

    new_style = "#{}: {:<10s} = {}".format(i + 1, item.title(), round(count))

    assert old_style == new_style

# Python 3.6 added interpolated format strings - f-strings for short
# completely elimintes the redundancy of providing keys and values to be formatted
# they achieve this by allowing you to reference all names in the current Python scope as part
# of a formatting expression
key = "my_var"
value = 1.234

formatted = f"{key} = {value}"
print(formatted)

formatted = f"{key!r:<10} = {value:.2f}"
print(formatted)

f_string = f"{key:<10} = {value:.2f}"
c_tuple = "%-10s = %.2f" % (key, value)
str_args = "{:<10} = {:.2f}".format(key, value)
str_kw = "{key:<10} = {value:.2f}".format(key=key, value=value)
c_dict = "%(key)-10s = %(value).2f" % {"key": key, "value": value}
assert c_tuple == c_dict == f_string
assert str_args == str_kw == f_string

for i, (item, count) in enumerate(pantry):
    old_style = "#%d: %-10s = %d" % (i + 1, item.title(), round(count))
    new_style = "#{}: {:<10s} = {}".format(i + 1, item.title(), round(count))
    f_string = f"#{i + 1}: {item.title():<10s} = {round(count)}"
    assert old_style == new_style == f_string

for i, (item, count) in enumerate(pantry):
    print(f"#{i + 1}: {item.title():<10s} = {round(count)}")

# python expressions may also appear within the format specifier options
places = 2
number = 1.2345
print(
    f"My number is {number:.{places}f}"
)  # .3f specifies how many decimal points to go to

"""
✦ C-style format strings that use the % operator suffer from a variety
of gotchas and verbosity problems.
✦ The str.format method introduces some useful concepts in its for-
matting specifiers mini language, but it otherwise repeats the mis-
takes of C-style format strings and should be avoided.
✦ F-strings are a new syntax for formatting values into strings that
solves the biggest problems with C-style format strings.
✦ F-strings are succinct yet powerful because they allow for arbi-
trary Python expressions to be directly embedded within format
specifiers
"""
