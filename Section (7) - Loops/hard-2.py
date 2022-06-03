from unicodedata import digit


N = int(input()) # 123

res = 0

while N != 0: # 123  12 
    digit1 = N % 10 # 3  2 1
    res = res*10 + digit1 # 3 32 321
    N //= 10 # 12  1  0

print(res, res*3)