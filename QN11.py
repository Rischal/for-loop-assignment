lst = [1, 2, 3, 4]
new_lst = []
for item in lst:
    if item != 3:
        new_lst.append(item)
new_lst.insert(1, 'a')
print(new_lst)