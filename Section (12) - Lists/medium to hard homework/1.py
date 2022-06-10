def find_most_freq(lst):
    mn , mx = min(lst), max(lst)
    freq_lst = [0] * (mx-mn+1)

    for value in lst:
        freq_lst[value - mn] +=1
    
    real_val = freq_lst.index(max(freq_lst)) + mn
    return real_val, freq_lst[real_val] + 1

lst = list(map(int, input().split()))
print(find_most_freq(lst))