N, M = map(int, input().split())

start = 1

while start <= N:
    start2 = 1
    while start2 <= M:
        print(start, ' x ', start2, ' = ', start*start2)
        start2 +=1
    start +=1