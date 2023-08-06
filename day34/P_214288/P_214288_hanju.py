def solution(k, n, reqs):
    # Ⅰ. 멘토들에게 타입 분배
    arr = [1]*k
    def type_distribute(t, remain):
        # 타입 분배가 완료되면 최저 대기시간 찾기
        if t == k-1:
            arr[t] += remain
            find_min_waiting()
            arr[t] -= remain
        # 첫번째 타입부터 시작하여 중복 조합을 구함
        else:
            for r in range(remain+1):
                arr[t] += r
                type_distribute(t+1, remain-r)
                arr[t] -= r
    
    # Ⅱ. 상담 진행하면서 최저 대기시간 찾기
    min_waiting = float("inf")
    def find_min_waiting():
        nonlocal min_waiting
        # 변수 설정
        end_times = [[0]*arr[i] for i in range(k)]  # 멘토별 상담 끝나는 시간
        total_waiting = 0  # 대기 시간을 기록할 변수
        # reqs를 처리하며 total_waiting구하기
        for s, p, t  in reqs:
            # 가장 빨리 끝나는 멘토와 끝나는 시간 찾기
            end_time = min(end_times[t-1])
            mentor_idx = end_times[t-1].index(end_time)
            # 요청 시간과 상담 시작 시간 비교
            start, waiting = (s, 0) if s > end_time else (end_time, end_time - s)
            # 대기 시간 갱신
            total_waiting += waiting
            # 상담 끝나는 시간 갱신
            end_times[t-1][mentor_idx] = start + p
        # 최저 대기 시간 갱신
        if total_waiting < min_waiting: min_waiting = total_waiting

    type_distribute(0, n-k)
    return min_waiting
    
print(solution(1,2,[[10, 60, 1],[15, 60, 1]]))


