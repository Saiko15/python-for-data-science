T = int(input())
while T > 0:
    a = 10000000
    N = int(input())
    while N > 0:
        X = int(input())
        if X < a:
            a = X
        N-=1
    print("Min value is: ", a)
    T-=1