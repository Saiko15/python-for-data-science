def is_sublist(lst1, lst2):
    if len(lst2) == 0:
        return True

    if len(lst2) > len(lst1):
        return False

    for idx in range(len(lst2)):
        idx_in_main = lst1.index(lst2[idx])
        if lst2[idx] not in lst1:
            return False
        
