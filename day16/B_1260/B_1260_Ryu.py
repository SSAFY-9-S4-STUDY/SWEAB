from collections import deque

N, M, V = map(int, input().split())

lst = [[] for _ in range(N + 1)]

for _ in range(M):
    n1, n2 = map(int, input().split())
    lst[n1].append(n2)
    lst[n2].append(n1)

stk = deque([V])
visited = [0 for _ in range(N + 1)]
while stk:
    cur = stk.pop()
    if visited[cur] == 0:
        visited[cur] = 1
        print(cur, end=' ')
        for i in sorted(lst[cur], reverse=1):
            if visited[i] == 0:
                stk.append(i)

print()

q = deque([V])
visited = [0 for _ in range(N + 1)]
visited[V] = 1
while q:
    cur = q.popleft()
    print(cur, end=' ')
    for i in sorted(lst[cur]):
        if visited[i] == 0:
            visited[i] = 1
            q.append(i)

print()