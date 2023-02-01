N = int(input())
print( '-1' if N in [4,7] else N//5 + (N%5) % 3 + (N%5)//3)