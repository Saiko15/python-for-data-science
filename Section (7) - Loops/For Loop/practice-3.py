N, M, W = map(int, input().split())
cnt = 0
for A in range(1, N+1):
    for B in range(A, M+1):
        C = A + B
        if 1<= C <= W :
            cnt += W - C + 1

print(cnt)