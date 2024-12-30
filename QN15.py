s = "Hello 123!"
digits = 0
letters = 0
spaces = 0
for char in s:
    if char.isdigit():
        digits += 1
    elif char.isalpha():
        letters += 1
    elif char == " ":
        spaces += 1
print(f"Digits: {digits}, Letters: {letters}, Spaces: {spaces}")