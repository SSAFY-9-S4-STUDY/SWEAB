from collections import Counter, defaultdict
from itertools import combinations_with_replacement
from heapq import heappush, heappop
def solution(k, n, reqs):
    answer = 1e9
    # 최소 한 명의 상담원이 존재하여야 하므로 n-k
    comb = combinations_with_replacement([i for i in range(k)], r=n-k)
    cases = []
    for case in comb:
        base = [1 for _ in range(k)]
        for c in case:
            base[c] += 1
        cases.append(base)
    # 참가자 데이터 가공
    participants = defaultdict(list)
    for start_time, minutes, category in reqs:
        participants[category].append([start_time, start_time + minutes])

    for case in cases:
        wait_time = 0
        # 각 유형에 대해 wait_time 계산하여 더하기
        for i in range(k):
            p_list = sorted(participants[i+1], key=lambda x:x[0])
            mento_list = [0 for _ in range(case[i])]
            for start_time, end_time in p_list:
                mento_list = sorted(mento_list)
                if mento_list[0] <= start_time:
                    mento_list[0] = end_time
                else:
                    temp_t = mento_list[0] - start_time
                    mento_list[0] = end_time + temp_t
                    wait_time += temp_t
            # 수행 중 만약 현재 최소값보다 길어지면 break
            if wait_time > answer:
                break
        if wait_time < answer:
            answer = wait_time
    return answer