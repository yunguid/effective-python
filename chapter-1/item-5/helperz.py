from urllib.parse import parse_qs

my_values = parse_qs("red=5&blue=0&green=", keep_blank_values=True)
print(repr(my_values))


print("Red:     ", my_values.get("red"))
print("Green:   ", my_values.get("green"))
print("Opacity: ", my_values.get("opacity"))

# Would be nice to have default to zero instead of None

# works because red key is present in my_values
red = my_values.get("red", [""])[0] or 0
# works because green is "" in my_values
green = my_values.get("green", [""])[0] or 0
# works because of our 'or' fallback
opacity = my_values.get("opacity", [""])[0] or 0

print(f"Red: {red!r}")
print(f"Green: {green!r}")
print(f"Opactiy: {opacity!r}")

# let's say we wanted to ensure all parameter values are converted to ints
red = int(my_values.get("red", [""])[0] or 0)  # this is too hard to read

red_str = my_values.get("red", [""])
red = int(red_str[0]) if red_str[0] else 0


# if you need to reuse this logic repeatedly, write a helper
def get_first_int(values, key, default=0):
    found = values.get(key, [""])
    if found[0]:
        return int(found[0])
    return default


green = get_first_int(my_values, "green")
print(green)


"""
- Python's syntax makes it easy to write single-line expressions that
  are overly comlpex
- Move these expressions into helpers and consider if/else as an alternative
  to Boolean operators or and and in expressions
"""
