N = int(input())
area = [[] for _ in range(N+1)]
for i in range(N-1):
    x, y = map(int,input().split())
    area[x].append(y)
    area[y].append(x)
# print(area)
# [[], [6, 4], [4], [6, 5], [1, 2, 7], [3], [1, 3], [4]]
par = [1000] + [0 for _ in range(N)]
q = [1]
while q:
    temp = q.pop(0)
    for nodes in area[temp]:
        if not par[nodes]:
            par[nodes] = temp
            q.append(nodes)
for i in range(2, N+1):
    print(par[i])