from operator import truediv


N = int(input())
is_prime = True

for i in range(2, N):
    if N % i == 0:
        is_prime = False
        break

if is_prime:
    print("YES")
else:
    print("NO")
