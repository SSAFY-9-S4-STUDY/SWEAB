from collections import defaultdict
from itertools import combinations_with_replacement

def solution(k, n, reqs):
    answer = 10e9
    # key가 상담유형, value가 [시작, 종료]
    info = defaultdict(list)
    for a, b, c in reqs:
        info[c].append([a, a+b])

    # 중복 조합 경우의 수
    # combinations = combinations_with_replacement([i+1 for i in range(k)], n-k)
    combinations = combinations_with_replacement([i for i in range(k)], n-k)
    cases = []
    
    for combination in combinations:
        case = [1 for _ in range(k)]
        for combi in combination:
            case[combi] += 1
        cases.append(case)
    
    # case = 각 유형별 멘토가 몇명인지
    for case in cases:
        wait = 0
        # 대기시간 계산
        # idx: 상담 유형 인덱스
        for idx in range(k):
            mento = [0 for _ in range(case[idx])]
            for start, end in info[idx+1]:
                # 상담이 더 빨리 끝나는 사람한테 보내기 위해 sort
                mento.sort()
                if mento[0] <= start:
                    mento[0] = end
                else:
                    wait_tmp = mento[0] - start
                    wait += wait_tmp
                    mento[0] = end + wait_tmp

            if wait >= answer:
                break
        
        answer = min(wait, answer)
    return answer


print(solution(3, 5, [[10, 60, 1], [15, 100, 3], [20, 30, 1], [30, 50, 3], [50, 40, 1], [60, 30, 2], [65, 30, 1], [70, 100, 2]]))
print(solution(2, 3, [[5, 55, 2], [10, 90, 2], [20, 40, 2], [50, 45, 2], [100, 50, 2]]))