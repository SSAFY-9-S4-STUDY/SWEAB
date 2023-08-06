def solution(ts, t1, t2, a, b, onboard):
    # Ⅰ. 변수 할당
    # 1. t1 < t2 < ts 되게 획일화
    if ts < t1: ts, t1, t2 = -ts, -t2, -t1, 
    # 2. onboard의 길이, 총 온도 범위
    N, M = len(onboard), ts-t1+1
    # 3. 각 시간대별 온도별 최저 비용을 계산하기 위한 이중배열 생성
    temp_limit = t2-t1+1  # 쾌적 온도 범위
    temp_out =  ts-t2  # 쾌적 온도를 벗어난 범위 
    min_cost_arr = [[100000]*temp_limit + [-1]*temp_out if onboard[i] else [100000] * M for i in range(N)]

    # Ⅱ. dp를 사용하여 정답 도출
    # 1. 다음 시간대 최저 비용 갱신 함수
    def update_min_cost(time, temp, cost):
        min_cost_arr[time][temp] = min(min_cost_arr[time][temp], cost)
    # 2. ts부터 시작하여 각 노드들을 돌며 최저비용 도출
    min_cost_arr[0][-1] = 0
    for time in range(N-1):
        for temp in range(M):
            # 현재 시간, 온도대의 최저 비용
            now_min_cost = min_cost_arr[time][temp]
            # 허용되지 않는 온도 범위면 패스
            if min_cost_arr[time][temp] < 0: continue
            # 온도 낮추기
            if temp != 0: update_min_cost(time+1, temp-1, now_min_cost + a)
            # 온도 유지하기
            if temp < temp_limit: update_min_cost(time+1, temp, now_min_cost + b)
            # 에어컨 끄기
            next_temp = temp if temp == M-1 else temp + 1
            update_min_cost(time+1, next_temp, now_min_cost)
    # 3. -1을 제외한 값 중에서 최저 비용 찾기
    min_cost = 100000
    for i in range(M):
        tmp = min_cost_arr[-1][i]
        if tmp > -1: min_cost = min(tmp, min_cost)

    return min_cost

print(solution(-10, -5, 5, 5, 1, [0, 0, 0, 0, 0, 1, 0]))