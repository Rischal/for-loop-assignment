lst = [1, 2, 3, 4, 5]
odd = []
even = []
for item in lst:
    if item % 2 == 0:
        even.append(item)
    else:
        odd.append(item)
print("Odd:", odd)
print("Even:", even)