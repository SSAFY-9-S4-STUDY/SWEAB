from collections import deque

N = int(input())
arr = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(N-1):
    node1, node2 = map(int, input().split())
    arr[node1].append(node2)
    arr[node2].append(node1)

queue = deque([1])

while queue:
    now = queue.popleft()
    for i in arr[now]:
        if visited[i] == 0:
            visited[i] = now
            queue.append(i)

temp = visited[2:]
for i in temp:
    print(i)