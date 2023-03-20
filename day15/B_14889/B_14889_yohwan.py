import sys
sys.stdin = open("sample.txt")

from itertools import combinations

N = int(input())
members = [list(map(int, input().split())) for _ in range(N)]

ans = 19000
num = []
for i in range(1, N + 1):
    num.append(i)

team_a = list(combinations(num, N//2))
for x in team_a:
    team_b = list(set(num) - set(x))

    stat_a = 0
    stat_b = 0
    com_team_a = list(combinations(x, 2))
    com_team_b = list(combinations(team_b, 2))

    for i, j in com_team_a:
        stat_a += members[i-1][j-1] + members[j-1][i-1]

    for i, j in com_team_b:
        stat_b += members[i-1][j-1] + members[j-1][i-1]

    if ans > abs(stat_a - stat_b):
        ans = abs(stat_a - stat_b)

print(ans)
