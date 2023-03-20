import sys
sys.stdin = open("sample.txt")


def tree(start):
    queue = [start]
    res = 1
    while queue:
        x = queue.pop(0)
        if visited[x] == 1:
            res = 0
        else:
            visited[x] = 1
            for y in graph[x]:
                if visited[y] == 1:
                    res = 0
                if visited[y] == 0:
                    queue.append(y)
    return res


tc = 0
n, m = map(int, input().split())
for _ in range(m):
    a, b = map(int, input().split())

    cnt = 0
    graph = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    if n > 0 and m > 0:
        graph[a].append(b)
        graph[b].append(a)

        for i in range(n+1):
            if visited[i] == 0:
                if tree(i) == 1:
                    cnt += 1
            else:
                continue

if cnt == 0:
    print("Case 3: No trees.")
elif cnt == 1:
    print("Case 2: There is one tree.")
elif cnt > 1:
    print(f'Case 1: A forest of {cnt} trees.')




