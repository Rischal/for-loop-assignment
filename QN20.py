sum_odd = 0
for num in range(1, 101):
    if num % 2 != 0:
        sum_odd += num
print(f"Sum of odd numbers: {sum_odd}")