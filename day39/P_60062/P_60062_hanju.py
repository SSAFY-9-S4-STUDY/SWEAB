from collections import deque

def solution(n, weak, dist):
    # 1. 변수 설정
    # 취약점 개수, 사람 수
    N, M = len(weak), len(dist)
    # dist를 내림차순으로 정렬
    dist.sort(reverse=True)
    # 취약점끼리의 거리 배열
    weak_dist = [n-weak[-1] + weak[0]] + [weak[i+1] - weak[i] for i in range(N-1)] 

    # 2. 경우의 수를 따져가며 최소 인원수 구하기 함수
    queue = deque([(weak[:], 0, 0)])
    while queue:
        # 남은 취약점, 사람수, 취약점수
        w, p, n = queue.popleft()
        # 사람수가 최대치를 넘겼으면 더 이상 진행 X
        if p == M: return -1
        # 아니면 탐색 진행
        for i in range(N):
            # 이미 탐색한 취약점이면 패스
            if not w[i]: continue
            # 아니면 오른쪽으로 탐색 진행
            w_tmp = w[:]  # 현재까지 점검한 취약점
            cnt = 0  # 지금 사람이 셀 취약점
            d = dist[p]  # 남은 거리
            while d >= 0 and w_tmp[i]:
                cnt += 1
                w_tmp[i] = 0
                i = (i+1)%N
                d -= weak_dist[i]
            # 탐색 기록을 큐에 저장
            # 취약점 보완이 끝났으면 사람수 반환
            if n + cnt == N: return p + 1
            queue.append((w_tmp, p + 1, n + cnt))

print(solution(12, 	[1, 5, 6, 10], [1, 2, 3, 4]))