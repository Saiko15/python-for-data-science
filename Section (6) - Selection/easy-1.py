# ● Read 2 integers A, B and print based on following cases:
# ○ if both are odd print their product A*B
# ○ if both are even print their division A/B (float division / assume B != 0)
# ○ if the first is odd and the second is even then find their sum A+B
# ○ if the first is even and the second is odd then find their subtraction A-B
# ● Inputs ⇒ outputs
# ○ 5 7 => 35
# ○ 12 2 => 6
# ○ 5 6 => 11
# ○ 12 3 => 9
a, b = map(int, input().split())

if a % 2 == 1 and b % 2 == 1:
    print(a * b)
elif a % 2 == 0 and b % 2 == 0 and b != 0:
    print(a/b)
elif a % 2 == 1 and b % 2 == 0:
    print(a+b)
elif a % 2 == 0 and b % 2 == 1:
    print(a-b)



