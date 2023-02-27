import sys

num_of_nodes = int(sys.stdin.readline())
num_of_edges = num_of_nodes - 1
link = [[] for _ in range(num_of_nodes + 1)]

for i in range(num_of_edges):
    parent, child = map(int, sys.stdin.readline().split())
    link[parent].append(child)
    link[child].append(parent)

parent_group = [0] * (num_of_nodes + 1)
start_node = 1
visited = [0 for _ in range(num_of_nodes + 1)]
queue = [start_node]

while queue:
    now = queue.pop(0)
    visited[now] = 1
    for child in link[now]:
        if visited[child]:
            continue
        # if child not in visited:  # 이게 문젠데...!!!!!!!!!!!
        queue.append(child)
        # visited.append(child)
        parent_group[child] = now

for i in range(2, num_of_nodes + 1):
    print(parent_group[i])