N = int(input())
x = 1

while N > 0:
    if x % 3 == 0 and not x % 4 == 0:
        print(x, end=' ')
        N -=1
    x+=1

