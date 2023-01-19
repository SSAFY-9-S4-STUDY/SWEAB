N = int(input())
target,cnt = N,0

while target != N or cnt == 0:
    N = (N % 10)*10 + (N//10 + N%10) % 10
    cnt += 1

print(cnt)