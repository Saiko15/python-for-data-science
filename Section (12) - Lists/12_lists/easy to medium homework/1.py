def is_increasing(lst):
    for i in range(1, len(lst)):
        if lst[i] < lst[i-1]:
            return "NO"  
    return "YES" 

lst = list(map(int, input().split()))
print(is_increasing(lst))
