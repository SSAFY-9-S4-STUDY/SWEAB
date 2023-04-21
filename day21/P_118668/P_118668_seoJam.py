from pprint import pprint

def solution(alp, cop, problems):

    max_alp = max_cop = 0
    for problem in problems:
        max_alp = max(max_alp, problem[0])
        max_cop = max(max_cop, problem[1])
    max_alp -= alp
    max_cop -= cop

    dp = list([100 for j in range(max_cop)] for i in range(max_alp))
    dp[0][0] = 0  # 출발점
    pprint(dp, width=500)
    for i in range(max_alp):
        for j in range(max_cop):
            # [1] 알파력 1시간 공부
            dp[i+1][j] = min(dp[i+1][j], dp[i][j] + 1)
            # [2] 코딩력 1시간 공부
            dp[i][j+1] = min(dp[i][j+1], dp[i][j] + 1)
            # [3] 문제 풀기
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                nal_req, nco_req = alp_req - alp, cop_req - cop
                # 문제 풀 수 있다면?
                if i >= nal_req and j >= nco_req:

                    if i+alp_rwd > max_alp and j+cop_rwd > max_cop:
                        dp[max_alp][max_cop] = min(dp[max_alp][max_cop], dp[i][j] + cost)
                    elif i+alp_rwd > max_alp:
                        dp[max_alp][j+cop_rwd] = min(dp[max_alp][j+cop_rwd], dp[i][j] + cost)
                    elif j+cop_rwd > max_cop:
                        dp[i+alp_rwd][max_cop] = min(dp[i+alp_rwd][max_cop], dp[i][j] + cost)
                    else:
                        dp[i+alp_rwd][j+cop_rwd] = min(dp[i+alp_rwd][j+cop_rwd], dp[i][j] + cost)

    pprint(dp)
    answer = dp[max_alp-1][max_alp-1]
    return answer


print(solution(0, 0, [[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]))