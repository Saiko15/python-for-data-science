num = int(input())

if num % 10 == num:
    print("1 digit")
elif num % 100 == num:
    print("2 digits")
elif num % 1000 == num:
    print("3 digits")
elif num % 10000 == num:
    print("4 digits")
elif num % 100000 == num:
    print("5 digits")
else:
    print("5+ digits")
