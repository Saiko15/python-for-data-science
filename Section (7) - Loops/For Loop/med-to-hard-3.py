cnt = 0

for a in range(1, 201):
    for b in range(1, 201):
        for c in range(1, 201):
            d = a+b-c
            if 1 <= d <= 200:
                cnt += 1
print(cnt)