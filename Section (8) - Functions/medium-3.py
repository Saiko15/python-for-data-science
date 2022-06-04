def is_prime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

def nth_prime(n):
    for idx, i in enumerate(range(n+1)):
        if not is_prime(i):
            idx -=1
    return i

print(nth_prime(6))
# print(is_prime(13))