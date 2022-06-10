def digits_freq(lst):
    freq_lst = [0] * 10
    for value in lst:
        while value != 0:
            digit = value % 10
            value //= 10
            freq_lst[digit] += 1

    for idx, item in enumerate(freq_lst):
        print(idx, item )


lst = list(map(int, input().split()))
digits_freq(lst)