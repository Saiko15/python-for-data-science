from unittest import result


x, y = map(int, input().split())

res = x ** y

sum = 1
while y > 0:
    sum *= x
    y -= 1
print(sum)

assert res == sum, 'Hmm' 