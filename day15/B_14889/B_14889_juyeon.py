from itertools import combinations

N = int(input())
S = [list(map(int,input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if j > i:
            S[i][j] += S[j][i]

all = list(range(N))

dif_min = 100

for k in combinations(list(range(N)),N//2):
    a_team = []
    for i in all:
        if i not in k:
            a_team.append(i)
    dif = 0
    for i in range(N//2 -1):
        for j in range(i+1, N//2):
            dif += S[k[i]][k[j]] - S[a_team[i]][a_team[j]]
    dif = abs(dif)
    if dif < dif_min:
        dif_min = dif
print(dif_min)