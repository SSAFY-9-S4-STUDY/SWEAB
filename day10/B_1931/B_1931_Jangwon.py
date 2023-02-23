import sys
N = int(sys.stdin.readline().rstrip())
num = []
for _ in range(N):
    s, e = map(int, sys.stdin.readline().rstrip().split())
    num.append([s, e])
num.sort(key=lambda x: (x[1], x[0]))

cnt = 1
tmp = num[0][1]

for i in range(1, N):
    if num[i][0] < tmp:
        continue
    else:
        cnt += 1
        tmp = num[i][1]

print(cnt)