def calculator(N,m):
    result = 0
    while not N % m:
        N = N // m
        result += 1
        if N == 1: 
            break
       
    return N, result 

T = int(input())
for i in range(T):
    N = int(input())
    N, a = calculator(N,2)
    N, b = calculator(N,3)
    N, c = calculator(N,5)
    N, d = calculator(N,7)
    N, e = calculator(N,11)
    print(f'#{i+1} {a} {b} {c} {d} {e}')