N = int(input())

if N < 10000:
    print("this is a small number")
else:
    last1 = (N % 10)
    last2 = ( (N // 10) % 10)
    last3 =  ((N//100) % 10 )
    sum_last3 = last1 + last2 + last3
    if sum_last3 % 2 ==1:
        print("this a great number")
    else:
        if last1 % 2 == 1 or last2 %2 == 1 or last3 % 2 == 1:
            print("this is a goog number")
        else:
            print("this is a bad number")


    