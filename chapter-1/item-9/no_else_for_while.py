"""
Python loops have an extra feature that is not available in most
other programming languages: You can put an else block immediately after
a loop's repeated interior block
"""

for i in range(3):
    print("Looooop", i)
else:
    print("else block bitch!")

"""
Why is this clause called else? Usually else means "do this if the block before
does not happen

Using a break statement in a loop skips the else block
"""
for i in range(3):
    print("loop", i)
    if i == 1:
        break
else:
    print("else block after break")

"""
Another suprise is that the else block runs immediately if you loop over an
empty sequence
"""
for x in []:
    print("never runs")
else:
    print("for else block!")

while False:
    print("never runs")
else:
    print("while else block")

"""
The rationale for these behaviors is that else blocks after loops are useful
when using loops to search for something.
For example, if we want to determine whether two numbers are coprime (their
only common divisor i 1).
"""
a = 4
b = 9

for i in range(2, min(a, b) + 1):
    print("Testing", i)
    if a % i == 0 and b % i == 0:
        print(f"{a} and {b} are not coprime for {i}")
        break
else:
    print("coprime")


def coprime(a, b):
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            print(f"{a} and {b} are not coprime for {i}")
            return False
    return True


assert coprime(4, 9)
assert not coprime(3, 6)


"""An alternate method for this is to have a result variable that indicates whether
I've found what I'm looking for in a loop. I break out of the loop as soon as I find it"""


def coprime_alternate(a, b):
    is_coprime = True
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            is_coprime = False
            break
    return coprime


assert coprime(4, 9)
assert not coprime(3, 6)


"""Notes:
    - avoid using else blocks after loops
    - python has special syntax which allows else blocks to immediately follow 'for' and 'while' loop
      interior blocks
"""
