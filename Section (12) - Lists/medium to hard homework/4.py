def recaman_seq(num):
    lst = [0] * (num) *10
    lst[0] = 0
    lst[1] = 1
    for i in range(2, num+1):
        value = lst[i-1] - (i-1) - 1
        if value > 0 and value not in lst:
            lst[i] = value
        else:
            lst[i] = lst[i-1] + (i-1) + 1

        return lst[num] 

num = int(input())
print(recaman_seq(num))
