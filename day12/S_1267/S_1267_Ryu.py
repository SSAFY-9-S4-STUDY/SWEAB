cases = 10
for x in range(1, cases + 1):
    V, E = map(int, input().split())
    suns = list(map(int, input().split()))
    needed = [[] for _ in range(V + 1)]
    can_go = [[] for _ in range(V + 1)]
    for i in range(E):
        f, t = suns[2 * i: 2 * i + 2]
        needed[t].append(f)
        can_go[f].append(t)

    q = []
    for i in range(1, V + 1):
        if not needed[i]:
            q.append(i)

    rlt = []

    while q:
        cur = q.pop(0)
        rlt.append(cur)
        for go in can_go[cur]:
            needed[go].remove(cur)
            if not needed[go]:
                q.append(go)

    print(f'#{x}', *rlt)