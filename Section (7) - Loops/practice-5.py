from ast import While


N = int(input())
copy = N

while N>0:
    x = copy
    while x >= N:
        print("*", end='')
        x-=1
    print('')
    N-=1