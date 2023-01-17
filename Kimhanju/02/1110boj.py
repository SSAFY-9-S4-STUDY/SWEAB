N = int(input())
new_N,n = N,0

while new_N != N or n == 0:
    N = (N % 10)*10 + (N//10 + N%10) % 10
    n += 1

print(n)