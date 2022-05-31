X ,s1, e1, s2, e2, s3, e3 = map(int, input().split())
count_intervals = 0

count_intervals += s1 <= X <= e1

count_intervals += s2 <= X <= e2

count_intervals += s3 <= X <= e3

print(count_intervals)
