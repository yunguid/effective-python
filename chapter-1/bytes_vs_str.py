# bytes vs strings in Python 3

print("=" * 40)
print("1. Basic types")
print("=" * 40)

a = b"h\x65llo"
print(f"bytes: {a} -> {list(a)} -> {type(a)}")

b = "a\u0300 propos"
print(f"str: {b} -> {list(b)} -> {type(b)}")

print("\n" + "=" * 40)
print("2. Conversion helpers")
print("=" * 40)


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


foo = b"foo"
print(f"to_str: {repr(to_str(foo))} | {repr(to_str('bar'))}")
print(f"to_bytes: {repr(to_bytes(b'foo'))} | {repr(to_bytes('bar'))}")

print("\n" + "=" * 40)
print("3. Concatenation")
print("=" * 40)

print("works:", b"one" + b"two", "|", "one" + "two")

try:
    "one" + b"two"
except Exception as e:
    print("fails:", type(e).__name__)

try:
    b"one" + "two"
except Exception as e:
    print("fails:", type(e).__name__)

print("\n" + "=" * 40)
print("4. Comparison")
print("=" * 40)

print(f"same type: {b'red' > b'blue'} | {'red' > 'blue'}")

try:
    "red" > b"blue"
except Exception as e:
    print(f"mixed type: {type(e).__name__}")

print(f"equality: {b'foo' == 'foo'}")

print("\n" + "=" * 40)
print("5. String formatting")
print("=" * 40)

print("works:", "Hello %s" % "World", "|", b"red %s" % b"blue")

try:
    b"hello %s" % "darling"
except Exception as e:
    print("fails:", type(e).__name__)

print("\n" + "=" * 40)
print("6. File I/O")
print("=" * 40)

with open("data.bin", "wb") as f:
    f.write(b"\xf1\xf2\xf3\xf4\xf5")

try:
    with open("data.bin", "r") as f:
        data = f.read()
except Exception as e:
    print("text mode fails:", type(e).__name__)

with open("data.bin", "rb") as f:
    data = f.read()
    print("binary mode works:", data)
