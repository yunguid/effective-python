"""
How to use open() in python

Also general information and review of reading and writing to files

open() returns a file object (also called a file handle)
You must pass in a path ot the file you want to open as a string
Optional arguments
- descriptions: string specifying how to open the file ("r", "w", "a", etc.)
-defaults to 'r'
... many more
"""

with open("example.txt", "r") as f:
    content = f.read()
    line = f.readline()
    lines = f.readlines()
    print(content)
    print(f"Line: {line}")
    print(f"Lines: {lines}")


with open("button.png", "rb") as f:
    data = f.read()
    print(f"Data of button.png: {data}")

# append mode
with open(file="example.txt", mode="a") as f:
    f.write("This will go at the end of the file, cheerio!")


# Seeking (move the file pointer)
with open("example.txt", "r") as f:
    f.seek(0)
    content = f.read(5)
    print(f"content: {content}")
    f.seek(10)
    part = f.read(10)
    print(f"seeked 10: {part}")
