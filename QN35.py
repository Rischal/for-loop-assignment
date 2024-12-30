total = 0
for num in range(3, 100):
    if num % 3 == 0 or num % 5 == 0:
        total += num
print(total)