from collections import deque
def solution(info, edges):
    n = len(info)
    tree = [[] for _ in range(n)]
    answer = 1  # 루트 노드는 양으로 고정됨.
    
    for p, c in edges:
        tree[p].append(c)
    
    q = deque([[tree[0], 1, 1]])

    while q:
        data = q.popleft()

        for i, next_node in enumerate(data[0]):
            total = data[2]
            if info[next_node] == 0:
                temp = data[1] + 1
                total += 1
            else:
                temp = data[1] - 1
            
            if temp > 0:
                q.append([data[0][:i] + data[0][i+1:] + tree[next_node], temp, total])
                answer = max(answer, total)
    
    return answer