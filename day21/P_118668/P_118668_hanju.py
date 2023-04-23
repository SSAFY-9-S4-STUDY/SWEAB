from collections import deque

def solution(alp, cop, problems):
    # problems을 순회하면서 목표치(달성할 코딩력과 알고력의 최대값) 갱신
    target_alp, target_cop = 0, 0
    for p in problems:
        if target_alp < p[0]:
            target_alp = p[0]
        if target_cop < p[1]:
            target_cop = p[1]
    problems += [[0,0,1,0,1], [0,0,0,1,1]]

    # max_time : 현재 상황에서 알고력과 코딩력을 기를 때 최대로 걸리는 시간
    # queue : 알고력, 코딩력, 걸린 시간을 튜플 형식으로 저장할 배열
    # time_record : 알고력, 코딩력 수치별 최단시간 기록을 위한 이중 배열
    max_time = max(target_alp-alp, 0) + max(target_cop-cop, 0)
    queue = deque([(min(alp, target_alp), min(target_cop, cop), 0)])
    time_record = [[max_time]*(target_alp+1) for _ in range(target_cop+1)]

    # 백트래킹과 DFS를 사용하여 완전탐색
    while queue:
        # a, c, t : 알고력, 코딩력, 걸린 시간
        a, c, t = queue.popleft()
        # pop한 시간이 해당 좌표에 기록된 최단 기록보다 작으면 패스
        if t > time_record[c][a]:
            continue
        # 채우지 못 했으면 문제들을 순회하며 DFS
        for p in problems:
            # 현재 해결할 수 없는 문제면 다음 문제로
            if a < p[0] or c < p[1]:
                continue
            # 해당 문제 해결 후 시간이 기록된 최단시간을 넘기지 않는다면 연산 진행
            # 그리고 최단 시간 기록 배열 또한 갱신해줌
            na, nc, nt = min(target_alp, a+p[2]),min(target_cop, c+p[3]), t+p[4]
            if nt < time_record[nc][na]:
                for i in range(nc, -1, -1):
                    if time_record[i][na] <= nt:
                        break
                    for j in range(na, -1, -1):
                        if time_record[i][j] <= nt:
                            break
                        time_record[i][j] = min(nt, time_record[i][j])
                # queue에 갱신값들을 넣어줌
                queue.append((na, nc, nt))

    return time_record[-1][-1]
            

alp, cop = 0, 0
problems = [[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]
print(solution(alp, cop, problems))