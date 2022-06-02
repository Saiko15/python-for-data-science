N = int(input())

x = 0
while x <=N:
    if x % 8 == 0 or (x % 4 ==0 and x % 3 == 0):
        print(x, end=' ')
    x +=1