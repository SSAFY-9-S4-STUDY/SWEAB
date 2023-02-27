import sys
sys.setrecursionlimit(10**5) 

def dfs(R):
    global v_lst, idx
    idx += 1
    v_lst[R] = idx
    for i in sorted(path[R]):
        if not v_lst[i]:
            dfs(i)
    return


N, M, R = map(int,input().split())
path = [[] for _ in range(N+1)]

for _ in range(M):
    x, y = map(int,input().split())
    path[x].append(y)
    path[y].append(x)
 

v_lst = [0 for _ in range(N+1)]  
idx = 0
dfs(R)
for i in range(1, N+1):
    print(v_lst[i])