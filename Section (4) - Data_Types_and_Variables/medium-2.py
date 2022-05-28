from posixpath import split


num1, num2 = map(int, input().split())

tmp = num1
num1 = num2
num2 = tmp

## num1, num2 = num2, num1

print(num1, num2)