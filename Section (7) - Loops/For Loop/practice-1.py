T = int(input()) # 2
for i in range(T): #
    N, res = int(input()), 0 # 3
    for j in range(N): # 0 1 2 
        a, it = int(input()), 1 # 5 7 2
        for k in range(j+1):
            it *= a # 49 8
        res += it # 5 54 62 
    print("Sum is: ", res) 
