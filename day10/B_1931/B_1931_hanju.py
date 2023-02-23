import sys

N = int(sys.stdin.readline())
meetings = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
meetings.sort(key = lambda x: (x[1], x[0]))

end, cnt = meetings[0][1], 1
for i in range(1,N):
    if meetings[i][0] >= end:
        cnt += 1
        end = meetings[i][1]

print(cnt)

