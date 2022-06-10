def find_smallest(lst, target_type):

    new_lst = [n for n in lst if type(n) == target_type]
    return min(new_lst)

lst = [10, -2.5, 20, 5, 'mostafa', 5.2, 'Ziad']

print(find_smallest(lst, type(0)))
print(find_smallest(lst, type(0.0)))
print(find_smallest(lst, type('')))
