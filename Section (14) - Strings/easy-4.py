S = input()
T = input()
new_str = ''

sz = min(len(S), len(T))


for i in range(sz):
    new_str = new_str + S[i] + T[i]

if len(T) > len(S):
    new_str += T[sz:]

if len(S) > len(T):
    new_str += T[sz:] 


print(new_str)