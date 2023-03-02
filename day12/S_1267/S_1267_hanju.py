import sys
sys.stdin = open('1267.txt', 'r')

for test_case in range(1, 11):
    V, E = map(int, input().split())

    parent = [[] for _ in range(V+1)]
    child = [[] for _ in range(V+1)]
    raw = list(map(int, input().split()))
    for i in range(E):
        p, c = raw[2*i], raw[2*i+1]
        parent[c].append(p)
        child[p].append(c)

    queue, done, in_que  = [], [0]*(V+1), [0]*(V+1)
    for i in range(1, V+1):
        if not parent[i]:
            queue.append(i)
            in_que[i] = 1

    sequence = []
    while queue:
        nod = queue.pop(0)

        progress = True
        for i in parent[nod]:
            if not done[i]:
                progress = False
                break

        else:
            sequence.append(nod)
            done[nod] = 1
            for j in child[nod]:
                if not in_que[j]:
                    queue.append(j)
                    in_que[j] = 1

        if not progress:
            queue.append(nod)
    
    print(f'#{test_case}', *sequence)

    


