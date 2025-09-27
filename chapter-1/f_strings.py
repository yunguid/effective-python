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

template = "%s loves food. Let that retard %s cook!"
name = "Luke"
formatted = template % (name, name)
print(formatted)
