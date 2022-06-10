def is_susequance(lst1, lst2):
    for idx in range(len(lst2)):
        if lst2[idx] not in lst1:
            return False
        elif idx != 0:
            if lst1.index(lst2[idx]) < lst1.index(lst2[idx-1]):
                return False
        
    return True

            

lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))

print(is_susequance(lst1, lst2))