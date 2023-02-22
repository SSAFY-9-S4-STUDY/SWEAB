N = int(input())

time_table = [list(map(int, input().split())) for _ in range(N)]
time_table.sort(key = lambda x: (x[1], x[0]))

cnt = 0
idx = 0
for meeting in time_table:
    if idx <= meeting[0]:
        cnt += 1
        idx = meeting[1]
print(cnt)