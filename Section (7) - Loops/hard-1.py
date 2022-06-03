N = int(input())

while N>0:
    S = input()
    if S == 'ON' or S == 'NO' or S == 'no' or S == 'on' or S == 'No' or S == 'nO' or S == 'On' or S == 'oN':
        print('Match: ', S)
    N-=1