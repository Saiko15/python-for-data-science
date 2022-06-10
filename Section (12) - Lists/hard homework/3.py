def fixed_slided_show(lst, N):
    max_sum = 0
    for idx in range(len(lst)-N+1):
        if sum(lst[idx:idx+N]) > max_sum:
            max_sum = sum(lst[idx:idx+N])
        
    return max_sum

lst = list(map(int, input().split()))
N= int(input())

print(fixed_slided_show(lst,N))