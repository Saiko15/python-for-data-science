N, M, SUM = map(int, input().split())
count = 0
for i in range(1,N):
    for j in range(1,M):
        if i + j == SUM:
            count +=1
    
print(count)
