s1, e1, s2, e2 = map(int, input().split())


if s1 <= s2 <= e1:
    print (s2, e1)
else:
    print(-1)