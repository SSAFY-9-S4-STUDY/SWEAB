from collections import deque

def solution(info, edges):
    res = 0
    N = len(info)
    # 입력값을 토대로 이진트리 표현하기
    child, parent = [[] for _ in range(N)], [-1] * N
    for p, c in edges:
        child[p].append(c)
        parent[c] = p
    # 이진트리를 순회하며 정답구하기
    # [다음 갈 수 있는 루트들, 양 마리수, 늑대 마리수, 현재 노드]
    queue = deque([([0] * N, 0, 0, 0)])
    while queue:
        next_nods, sheep, wolf , pos = queue.popleft()
        # 양, 늑대 마리수 갱신
        if info[pos]: wolf += 1
        else: sheep += 1
        # 양과 늑대의 수가 같다면 그 경로는 사용 불가
        if sheep == wolf:
            continue
        # 루트가 유효하다면 우선 양의 최대 마리 갱신
        res = max(res, sheep)
        # 루트가 유효하다면 현재 위치 방문 처리
        next_nods[pos] = 0
        # 이후 다음 방문할 노드와 상태 정보들을 큐에 저장
        for c in child[pos]:
            next_nods[c] = 1
        for next in range(N):
            if next_nods[next]:
                queue.append((next_nods[:], sheep, wolf, next))

    return res

        
        
print(solution([0,0,1,1,1,0,1,0,1,0,1,1],[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))
