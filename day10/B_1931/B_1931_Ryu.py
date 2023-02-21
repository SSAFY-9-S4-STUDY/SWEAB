import sys
input = sys.stdin.readline

num = int(input())

lst = [list(map(int, input().split())) for _ in range(num)]
lst.sort(key = lambda x : x[0])
lst.sort(key = lambda x : x[1])

n = 0
cnt = 0
for i in lst:
    if n <= i[0]:
        n = i[1]
        cnt += 1

print(cnt)
