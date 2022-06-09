def our_reverse(lst):

    for idx in range(len(lst)//2):
        last = len(lst) - idx - 1
        tmp = lst[idx]
        lst[idx] = lst[last]
        lst[last] = tmp
        # lst[idx], lst[last] = lst[last], lst[idx]

    return lst
    

lst = list(map(int, input().split()))

print(our_reverse(lst))