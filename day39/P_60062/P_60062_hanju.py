from itertools import combinations

def solution(n, weak, dist):
    # 1. 변수 설정
    # 취약점 개수, 사람 수
    N, M = len(weak), len(dist)
    # dist를 내림차순으로 정렬
    dist.sort(reverse=True)
    # 취약점끼리의 거리 
    weak_dist = [weak[i+1] - weak[i] for i in range(N-1)] + [n-weak[-1] + weak[0]]

    # 2. 조합을 이용하여 탐색 거리를 제외
    for n in range(1, M+1):
        for comb in combinations(range(N), n):
            now_weak_dist = weak_dist[:]
            # 선택된 탐색거리 삭제
            for idx in comb: now_weak_dist[idx] = 0
            # 남은 탐색거리들을 등분해서 정리
            d_parts, now_d = [], 0
            for _ in range(N):
                idx -= 1
                if not now_weak_dist[idx]:
                    d_parts.append(now_d)
                    now_d = 0
                else: now_d += weak_dist[idx]
            # 등분한 탐색거리를 정렬
            d_parts.sort(reverse=True)
            # 등분한 탐색거리를 친구들에게 분배
            for i in range(n):
                if d_parts[i] > dist[i]: break
            else: return n

    return -1

print(solution(12, 	[1, 3, 4, 9, 10], [3, 5, 7]))