cnt = 0

for X in range(50, 301):
    for Y in range(70, 401):
        if X < Y and ((X+Y) % 7 == 0):
            cnt += 1


print(cnt)