def comb(cnt, idx, rst):
    global min_dif
    if cnt == N//2:
        dif = total
        for i in rst:
            dif -= sum(synergy[i])
            dif -= sum(synergy_trans[i])
        min_dif = min(min_dif, abs(dif))

    else:
        for i in range(idx, N-N//2+cnt+1):
            comb(cnt + 1, i+1, rst + [i])


N = int(input())
synergy = [list(map(int, input().split())) for _ in range(N)]
synergy_trans = list(zip(*synergy))

total = sum(sum(synergy,[]))
min_dif = 100*N*N
comb(1, 1, [0])

print(min_dif)