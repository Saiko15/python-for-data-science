lst = list(map(int, input().split()))
new_lst = []

for value in lst:
    if value not in new_lst:
        new_lst.append(value)

print(new_lst)