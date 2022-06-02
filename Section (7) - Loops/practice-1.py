num = int(input())

x = 1
while x <= num:
    if x % 3 == 0:
        print(x)
        x += 3
    else:
        x +=1
    
    