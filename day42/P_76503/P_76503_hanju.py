from collections import deque

def solution(a, edges):
    # 1. 가중치를 모두 0으로 만들 수 없는 경우
    if sum(a) != 0: return -1

    # 2. 변수 설정
    # 노드 개수
    N = len(a)
    # 노드간 연결 관계를 표현할 이중 배열
    connections = [[] for _ in range(N)]
    for nod1, nod2 in edges:
        connections[nod1].append(nod2)
        connections[nod2].append(nod1)
    # bfs를 시작할 리프 노드
    queue = deque([])
    for i in range(N):
        if len(connections[i]) == 1: queue.append(i)
    
    # 3. 임의로 루트 노트를 설정하여 트리의 부모 자식 관계 정의
    visited = [0] * N
    child_parent = []
    queue = deque([0])
    while queue:
        parent = queue.popleft()
        visited[parent] = 1
        for child in connections[parent]:
            if visited[child]: continue
            queue.append(child)
            child_parent.append([child, parent])
    
    # 4. 트리를 순회하며 가중치 0으로 만들기
    answer = 0
    for c, p in child_parent[::-1]:
        a[p] += a[c]
        answer += abs(a[c])
        a[c] = 0

    return answer
            



print(solution([-5,0,2,1,2], [[0,1],[3,4],[2,3],[0,3]]))