car_ages = [0, 9, 4, 8, 7, 20, 19, 1, 6, 15]
car_ages_descending = sorted(car_ages, reverse=True)
oldest = car_ages_descending[0]
second_oldest = car_ages_descending[1]
others = car_ages_descending[2:]
print(oldest, second_oldest, others)

# catch all unpacking through a starred expression
oldest, second_oldest, *others = car_ages_descending
print(oldest, second_oldest, others)

# can appear in any position
oldest, *others, youngest = car_ages_descending
print(oldest, youngest, others)


*others, second_youngest, youngest = car_ages_descending
print(youngest, second_youngest, others)


nums = [1, 2, 3, 4, 5, 6, 6, 3]
a, *b, c = nums
# c = nums  # cannot do *c on its own
print(a, b, c)


# can't use multiple starred expressions in an unpacking assignment statement
# can do it in this context
car_inventory = {
    "downtown": ("silver shadow", "pinto", "dmc"),
    "airport": ("skyline", "viper", "gremlin", "nova"),
}
((loc1, (best1, *rest1)), (loc2, (best2, *rest2))) = car_inventory.items()
print(f"Best at {loc1} is {best1}, {len(rest1)} others")
print(f"Best at {loc2} is {best2}, {len(rest2)} others")


short_list = [1, 2]
first, second, *rest = short_list
print(first, second, rest)


# unpack arbitrary iterators with unpacking syntax
it = iter(range(1, 3))
first, second = it
print(f"{first} and {second}")


def generate_csv():
    yield ("Date", "Make", "Model", "year", "price")
    yield ("2024-01-01", "Toyota", "Camry", 2020, 25000)
    yield ("2024-01-02", "honda", "civic", 2021, 24000)


all_csv_rows = list(generate_csv())
for row in generate_csv():
    print(row)
header, *rows = generate_csv()
print(f"Header: {header}, Rows: {rows}")


"""
Unpacking assignments may use a starred expression to catch all values that
weren't assigned to the other parts of the unpacking pattern into a list

Starred expressions may appear in any position, and they will always
become a list containing the zero or more values they receive

When dividing a list into non-overlapping pieces, catch all unpacking is much less error
prone than slicing and indexing

"""
