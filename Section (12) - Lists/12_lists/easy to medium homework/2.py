def replace_min_max_inplace(lst):
    max_num = max(lst)
    min_num = min(lst)
    for i in range(len(lst)):
        if lst[i] == max_num:
            lst[i] = min_num
        elif lst[i] == min_num:
            lst[i] = max_num


lst = list(map(int, input().split()))
replace_min_max_inplace(lst)
for i in lst:
    print(i, end=' ')
