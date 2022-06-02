N = int(input())
total = N/2
odd_sum = even_sum = 0
while N > total:
    a = int(input())
    b = int(input())
    odd_sum += a
    even_sum += b
    N -=1

odd_avg = odd_sum / (total)
even_avg = even_sum / (total)
print(odd_sum, even_sum)
print(odd_avg, even_avg)