def split_string(str): #111222aabbb
    str = str + "$"
    new_str =[]
    idx = 0
    for i in range(1,len(str)):
        if str[i] != str[i-1]:
            new_str.append(str[idx:i])
            idx = i
        
    return new_str

print(','.join(split_string("111222aabbb")))