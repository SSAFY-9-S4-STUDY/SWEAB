from collections import deque

def solution(n, s, a, b, fares):
    # 노드간 요금 정보 입력
    fares_dict = {i:{i:0} for i in range(1, n+1)}
    for n1, n2, p in fares:
        fares_dict[n1][n2] = p
        fares_dict[n2][n1] = p
    
    # 각 노드에서 s, a, b 노드로의 최단 거리 합
    min_totals = [0] * (n+1)

    # s, a, b 노드로부터의 최단 거리 각각 구하기
    for target in (s, a, b):
        # 각 노드로부터의 최단 거리를 나타낼 배열
        min_tmp  = [100000*n] * (n+1)
        # bfs와 dp를 이용해 최단 거리들 구하기
        queue = deque([(target, 0)])
        while queue:
            # 현재 위치까지의 거리가 기록된 최소값보다 작다면 최솟값 갱싱
            now_nod, fare = queue.popleft()
            if fare < min_tmp[now_nod]:
                min_tmp[now_nod] = fare
                # 연결된 노드 큐에 넣기
                for next_nod in fares_dict[now_nod]:
                    queue.append((next_nod, fare+fares_dict[now_nod][next_nod]))
        
        # 최단 거리의 합 갱신
        min_totals = [min_totals[i]+min_tmp[i] for i in range(n+1)]

    # 최단 거리의 합이 가장 적은 노드의 값을 반환
    return min(min_totals)
        





n, s, a, b = 6, 4, 6, 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
print(solution(n, s, a, b, fares))