def find_3_min(lst):
    mn1, mn2, mn3 = min(lst), lst[0], lst[1]
    if len(lst) <= 3:
        return sorted(lst)
    
    if mn2 > mn3:
        mn2, mn3 = mn3, mn2

    for idx in range(2, len(lst)):
        if lst[idx] < mn2 and lst[idx] != mn1:
            mn3 = mn2
            mn2 = lst[idx]
        
    return mn1, mn2, mn3

lst = list(map(int, input().split()))
print(find_3_min(lst))
