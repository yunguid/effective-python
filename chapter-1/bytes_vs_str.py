# ============================================================================
# BYTES vs STRINGS in Python 3
# ============================================================================

print("=" * 60)
print("SECTION 1: Basic bytes and str differences")
print("=" * 60)

# Bytes literal with hex escape sequence
a = b"h\x65llo"
print(f"Bytes literal: {a}")
print(f"As list of integers: {list(a)}")
print(f"Type: {type(a)}")

print()

# Unicode string with combining character
b = "a\u0300 propos"
print(f"Unicode string: {b}")
print(f"As list of characters: {list(b)}")
print(f"Type: {type(b)}")

print("\n" + "=" * 60)
print("SECTION 2: Helper functions for conversion")
print("=" * 60)


def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode("utf-8")
    else:
        value = bytes_or_str
    return value


def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode("utf-8")
    else:
        value = bytes_or_str
    return value


# Testing conversion functions
foo = b"foo"
print(f"Original bytes: {type(foo)} -> {repr(foo)}")
print(f"to_str(bytes): {repr(to_str(foo))}")
print(f"to_str(str): {repr(to_str('bar'))}")

print()

print(f"to_bytes(bytes): {repr(to_bytes(b'foo'))}")
print(f"to_bytes(str): {repr(to_bytes('bar'))}")

print("\n" + "=" * 60)
print("SECTION 3: Concatenation - Same types work, mixed types fail")
print("=" * 60)

# Same types work fine
print("✓ bytes + bytes:", b"one" + b"two")
print("✓ str + str:", "one" + "two")

print("\n--- Attempting mixed type concatenation (will fail) ---")

try:
    result = "one" + b"two"
    print(f"str + bytes: {result}")
except Exception as e:
    print(f"✗ ERROR (str + bytes): {type(e).__name__}: {e}")

try:
    result = b"one" + "two"
    print(f"bytes + str: {result}")
except Exception as e:
    print(f"✗ ERROR (bytes + str): {type(e).__name__}: {e}")

print("\n" + "=" * 60)
print("SECTION 4: Comparison operations")
print("=" * 60)

print("--- Same type comparisons (work fine) ---")
print(f"b'red' > b'blue': {b'red' > b'blue'} (lexicographic order)")
print(f"'red' > 'blue': {'red' > 'blue'} (ASCII: 'r'=114 > 'b'=98)")

print("\n--- Mixed type comparison (will fail) ---")
try:
    result = "red" > b"blue"
    print(f"'red' > b'blue': {result}")
except Exception as e:
    print(f"✗ ERROR (str > bytes): {type(e).__name__}: {e}")

print("\n--- Equality comparison between different types ---")
print(f"b'foo' == 'foo': {b'foo' == 'foo'} (different types are never equal)")

print("\n" + "=" * 60)
print("SECTION 5: String formatting with % operator")
print("=" * 60)

print("--- Same type formatting (works fine) ---")
print(f"str formatting: {'Hello %s' % 'World'}")
print(f"bytes formatting: {b'red %s' % b'blue'}")

print("\n--- Mixed type formatting (will fail) ---")
try:
    result = b"hello %s" % "darling"
    print(f"bytes % str: {result}")
except Exception as e:
    print(f"✗ ERROR (bytes % str): {type(e).__name__}: {e}")

print("\n" + "=" * 60)
print("SECTION 6: File I/O - Text vs Binary modes")
print("=" * 60)

# Write binary data to file
print("Writing binary data to 'data.bin'...")
with open("data.bin", "wb") as f:
    f.write(b"\xf1\xf2\xf3\xf4\xf5")

print("\n--- Attempting to read binary file in text mode (will fail) ---")
try:
    with open(file="data.bin", mode="r") as f:
        data = f.read()
    print(f"Text mode read: {data}")
except Exception as e:
    print(f"✗ ERROR (text mode on binary data): {type(e).__name__}: {e}")

print("\n--- Reading binary file in binary mode (correct way) ---")
with open(file="data.bin", mode="rb") as f:
    data = f.read()
    print(f"✓ Binary mode read: {data}")
