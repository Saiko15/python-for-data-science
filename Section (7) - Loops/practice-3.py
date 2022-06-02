from itertools import count


num = int(input())

count_len = 0

while num != 0:
    num = num // 10
    count_len +=1

print(count_len)