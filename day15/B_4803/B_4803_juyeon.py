def find_tree(x):
    global v
    
    res = True
    q = [x]
    while q:
        k = q.pop(0)
        if v[k]:
            res = False
        v[k] = 1
        for node in tree[k]:
            if not v[node]:
                q.append(node)
    return res
    
idx = 0
while True:
    idx += 1
    n, m = map(int, input().split())
    if not n:
        break
    tree = [[] for _ in range(n+1)]
    v = [0] *(n+1)

    for i in range(m):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)

    cnt = 0
    for i in range(1, n+1):
        if v[i]:
            continue
        if find_tree(i):
            cnt += 1

    if not cnt:
        print(f'Case {idx}: No trees.')
    elif cnt == 1:
        print(f'Case {idx}: There is one tree.')
    else:
        print(f'Case {idx}: A forest of {cnt} trees.')