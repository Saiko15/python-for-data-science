# ● Read an integer N (1 <= N <= 10)
# ● Then read N numbers, find which of them has the biggest value and print it.
# ● Inputs (but they will be on seperate lines)
# ○ 5 1 3 2 4.5 2 ⇒ 4.5
# ■ 5 means read 5 integers
# ■ Then we read them [1 3 2 4.5 2]. Their maximum is 4.5
# ○ 10 1 67 -9 88 -45 129 90 65 77 34 ⇒ 129
# ■ Same as last homework. This time we are given first N (10)
N = int(input())
a = -1000000

if N > 1:
    b = float(input())
    if a < b:
        a = b

if N > 2:
    b = float(input())
    if a < b:
        a = b

if N > 3:
    b = float(input())
    if a < b:
        a = b

if N > 4:
    b = float(input())
    if a < b:
        a = b

if N > 5:
    b = float(input())
    if a < b:
        a = b

if N > 6:
    b = float(input())
    if a < b:
        a = b

if N > 7:
    b = float(input())
    if a < b:
        a = b

if N > 8:
    b = float(input())
    if a < b:
        a = b

if N > 9:
    b = float(input())
    if a < b:
        a = b

if N > 10:
    b = float(input())
    if a < b:
        a = b



print(a)

