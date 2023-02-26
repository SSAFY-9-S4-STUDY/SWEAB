from collections import deque

N, M, R = map(int, input().split())
arr = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(M):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

for i in range(N+1):
    arr[i].sort()

queue = deque([R])
visited[R] = 1
count = 2

while queue:
    now = queue.popleft()
    for i in arr[now]:
        if visited[i] == 0:
            visited[i] = count
            queue.append(i)
            count += 1

temp = visited[1:]
for i in temp:
    print(i)



# arr = [[0] * (N + 1) for _ in range(N + 1)]
# visited = [0] * (N+1)
#
# for _ in range(M):
#     u, v = map(int, input().split())
#     arr[u][v] = 1
#     arr[v][u] = 1
#
# queue = deque([R])
#
# while queue:
#     now = queue.pop(0)
#     if visited[now]:
#         break
#     visited[now] = 1
#     for next in range(1, N+1):
#         if arr[now][next] == 1 and visited[next] == 0:
#             queue.append(next)
#     print(now)
# print(0)