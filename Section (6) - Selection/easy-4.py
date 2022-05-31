X = int(input())
a, b, c, d, e= map(int, input().split())

less_than_x = more_than_x = 0

if a <= X:
    less_than_x +=1
else:
    more_than_x +=1

if b <= X:
    less_than_x +=1
else:
    more_than_x +=1

if c <= X:
    less_than_x +=1
else:
    more_than_x +=1

if d <= X:
    less_than_x +=1
else:
    more_than_x +=1

if e <= X:
    less_than_x +=1
else:
    more_than_x +=1

print(less_than_x, more_than_x)
print("less_than_x =", less_than_x / more_than_x, " more_than_x")