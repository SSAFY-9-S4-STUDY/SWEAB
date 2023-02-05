N = int(input())

def hanoi(N, a, b):
    if N > 1:
        hanoi(N-1, a, 6-a-b)
    
    print(a, b)
    if N > 1:
        hanoi(N-1, 6-a-b, b)

print(2**N - 1)
hanoi(N, 1, 3)