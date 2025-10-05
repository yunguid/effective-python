"""
In addition to basic slicing, Python has special syntax for the stride of a slice

somelist[start:end:stride] - start, stop, step
"""

import logging

# Configure logging to show info level messages with timestamps
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%H:%M:%S",
)

print("=== BASIC STRIDE EXAMPLES ===")
logging.info("Starting basic stride examples")

x = ["red", "orange", "yellow", "green", "blue", "purple"]
print(f"Original list: {x}")
logging.info(f"Created list with {len(x)} elements: {x}")

logging.info("Performing x[::2] to get every 2nd element starting from index 0")
odds = x[::2]
logging.info("Performing x[1::2] to get every 2nd element starting from index 1")
evens = x[1::2]

print(f"Every 2nd element starting from index 0 (x[::2]): {odds}")
print(f"Every 2nd element starting from index 1 (x[1::2]): {evens}")
logging.info(f"Results - odds: {len(odds)} elements, evens: {len(evens)} elements")

"""
problem is that the stride syntax often causes unexpected behavior that can
introduce bugs.
For example, a common python trick for reversing a byte string is to slice the string
with a stride of -1
"""
print("\n=== REVERSING WITH NEGATIVE STRIDE ===")
logging.info("Demonstrating string reversal with negative stride")

x = b"mongoose"
print(f"Original byte string: {x}")
logging.info("Using [::-1] on byte string to reverse")
y = x[::-1]
print(f"Reversed with [::-1]: {y}")
logging.info(f"Byte string reversed: {x} -> {y}")

x = "apple"
print(f"Original string: '{x}'")
logging.info("Using [::-1] on regular string to reverse")
y = x[::-1]
print(f"Reversed with [::-1]: '{y}'")
logging.info(f"String reversed: '{x}' -> '{y}'")

# w = "無無"
# x = w.encode("utf-8")
# y = x[::-1]
# z = y.decode("utf-8")

print("\n=== COMPLEX STRIDE EXAMPLES ===")
logging.info("Starting complex stride examples - these can be confusing!")

x = ["a", "b", "c", "d", "e", "f", "g", "h"]
print(f"Original list: {x}")
logging.info(f"Working with list of {len(x)} elements: {x}")

logging.info("Executing x[::2] - start at beginning, no end specified, step by 2")
result1 = x[::2]
print(f"x[::2] (every 2nd element): {result1}")

logging.info("Executing x[::-2] - start at end, no beginning specified, step by -2")
result2 = x[::-2]
print(f"x[::-2] (every 2nd element, reversed): {result2}")

logging.info("Executing x[2::2] - start at index 2, no end specified, step by 2")
result3 = x[2::2]
print(f"x[2::2] (every 2nd element starting from index 2): {result3}")

logging.info(
    "Executing x[-2::-2] - start at 2nd-to-last element, go to beginning, step by -2"
)
result4 = x[-2::-2]
print(f"x[-2::-2] (every 2nd element from 2nd-to-last, going backwards): {result4}")

logging.info("Executing x[2:2:-2] - start at index 2, end at index 2, step by -2")
result5 = x[2:2:-2]
print(f"x[2:2:-2] (start at index 2, end at index 2, step -2): {result5}")
logging.warning(
    "Notice that x[2:2:-2] returns an empty list - this is often unexpected!"
)

print("\n=== CHAINING OPERATIONS (BETTER APPROACH) ===")
print("Instead of complex single expressions, break them into steps:")
logging.info(
    "Demonstrating better approach: breaking complex operations into clear steps"
)

logging.info("Step 1: Extract every 2nd element using x[::2]")
y = x[::2]
print(f"Step 1 - Extract every 2nd element: {y}")

logging.info("Step 2: Remove first and last elements using y[1:-1]")
z = y[1:-1]
print(f"Step 2 - Remove first and last elements: {z}")
logging.info(f"Final result after 2 clear steps: {z}")
logging.info("This approach is much clearer than a single complex slice expression!")
