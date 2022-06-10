def who_is_winner(N, K):
    num = 0
    print("people removed in order: ", end=' ')
    for i in range(1,N+1):
        num+= K
        print(num, end=' ')



N = int(input())
K = int(input())