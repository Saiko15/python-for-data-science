num = int(input()) # 391

years = num // 360  # 1
num = num % 360 # 31

months = num // 30 # 1
num = num % 30 # 1

print(years, months, num)