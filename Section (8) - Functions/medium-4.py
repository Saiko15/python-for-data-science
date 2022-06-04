def nth_fib(n):
    fib = 0
    for i in range(1,n):
        if i == 1:
            return 0
        elif i == 2:
            return 1
        else:
            return n + nth_fib(n-1)

print(nth_fib(5))