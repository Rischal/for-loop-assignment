lst = [1, 2, 3, 4, 5, 6, 7, 8]
even_count = 0
odd_count = 0
for num in lst:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print(f"Even numbers: {even_count}, Odd numbers: {odd_count}")