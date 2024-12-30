lst = [1, 2, 3, "d", 4, 5, "a"]
ints = []
strings = []
for item in lst:
    if isinstance(item, int):
        ints.append(item)
    elif isinstance(item, str):
        strings.append(item)
print("Integers:", ints)
print("Strings:", strings)