N = int(input())

if N % 2 == 0:
    print(N%10)
else:
    if N < 1000:
        print(N%100)
    else:
        if N < 1000000:
            print(N%10000)
        else:
            print(N * -1)