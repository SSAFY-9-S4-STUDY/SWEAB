from collections import defaultdict, deque
def solution(a, edges):
    if sum(a):
        return -1
    answer = 0
    tree = defaultdict(list)
    for edge in edges:
        tree[edge[0]].append(edge[1])
        tree[edge[1]].append(edge[0])
    
    queue = deque([])
    visited = [0 for _ in range(len(a))]
    for i in range(len(a)):
        if a[i]:
            queue.append(i)
            visited[i] = 1
            break
    route = []
    while queue:
        current_node = queue.popleft()
        route.append(current_node)
        for node in tree[current_node]:
            if visited[node] == 0:
                visited[node] = 1
                queue.append(node)
    
    visited = [0] * len(a)
    for i in range(len(a)-1, -1,-1):
        node = route[i]
        visited[node] = 1

        if a[node]:
            for v in tree[node]:
                if visited[v] == 0 and a[node]:
                    a[v] += a[node]
                    answer += abs(a[node])
                    a[node] = 0
    return answer

import time

array = [i for i in range(100, -1, -1)]
start = time.time()
array.sort()
end = time.time()
print(end-start)