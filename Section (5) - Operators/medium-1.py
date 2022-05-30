num = int(input())

is_even1 = (num % 2) == 0

is_even2 =   ( ( (num % 10) / 2) - ((num%10)//2) ) == 0

is_even3 =  ( (num / 2) - (num//2) ) == 0

print(is_even1, is_even2, is_even3)