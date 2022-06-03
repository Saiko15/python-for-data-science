from struct import unpack


N, A, B = map(int, input().split())

res = 0

for i in range(1, N+1):
    tmp = i
    digits = 0
    while tmp > 0:
        digits += tmp % 10
        tmp //= 10


    if A <= digits <=B:
        res+=i

print(res)


    
    