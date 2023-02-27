def bfs(R , q):
    global v_lst, idx 
    q.append(R)
    idx += 1
    v_lst[R] = idx
    while q:
        temp = q.pop(0)
        for i in sorted(path[temp]):
            if not v_lst[i]:
                q.append(i)
                idx += 1
                v_lst[i] = idx



N, M, R = map(int,input().split())
path = [[] for _ in range(N+1)]

for _ in range(M):
    x, y = map(int,input().split())
    path[x].append(y)
    path[y].append(x)


v_lst = [0 for _ in range(N+1)]
idx = 0
q = []
bfs(R, q)
for i in range(1, N+1):
    print(v_lst[i])