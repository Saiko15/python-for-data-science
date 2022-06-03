T = int(input())

while T > 0:
    N = int(input())
    res = 0
    start = 1
    while start <= N:
        num = int(input())
        res += num**start
        start +=1
    print("Sum is ", res)
    T-=1