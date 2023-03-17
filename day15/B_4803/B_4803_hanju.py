import sys

test_case = 0
while True:
    # 정점과 간선 개수 입력받기
    N, M = map(int, sys.stdin.readline().split())

    # 입력 종료인지 판단
    if N == 0 and M == 0:
        break
    
    # 각 정점들의 연결 관계 파악
    edges = [[] for _ in range(N)]
    for _ in range(M):
        nod1, nod2 = map(int, sys.stdin.readline().split())
        edges[nod1-1].append(nod2-1)
        edges[nod2-1].append(nod1-1)
    
    # 트리인지 확인
    visited, cnt = [0] * N, 0
    for nod in range(N):
        # 이미 방문한 노드라면 다음으로 넘어감
        if visited[nod]: 
            continue    
        visited[nod] = 1
        # DFS를 활용하여 트리 탐색
        stack = [nod]
        while stack:
            tmp = stack.pop()
            for i in edges[tmp]:
                # 이미 방문한 지점을 방문하게 되면 순환한다는 뜻
                # 트리가 아니므로 반복문 종료
                if visited[i]:
                    stack = 0
                    break
                # tmp는 간선 리스트에서 제외
                edges[i].remove(tmp)
                stack.append(i)
                visited[i] = 1
        # stack 빈 리스트(안전하게 종료)면 트리라 판단
        if stack != 0:
            cnt += 1

    # 정답 입력
    if cnt == 0:
        ans = 'No trees.'
    elif cnt == 1:
        ans = 'There is one tree.'
    else:
        ans = f'A forest of {cnt} trees.'

    test_case += 1
    print(f'Case {test_case}:',ans)