def solution(alp, cop, problems):
    # 필요한 알고력과 코딩력의 최댓값 구하기
    problems_t = list(zip(*problems))
    max_alp, max_cop = max(problems_t[0]), max(problems_t[1])

    # 처음에 이거 안썼더니 몇개 tc에서 런타임에러,,ㅠㅠ
    alp = min(alp, max_alp)
    cop = min(cop, max_cop)

    # 방법1 - dp 배열의 값을 최댓값으로 정의해주고 알고력, 코딩력 하나씩 늘리는 경우를 for문 안에 넣기
    # costs = [[300] * (max_cop + 1) for _ in range(max_alp + 1)]
    # costs[alp][cop] = 0

    # 방법2 - 그냥 공부해서 알고력 코딩력을 늘린다고 가정했을 때의 비용을 미리 dp에 반영/ 2중 for문의 if문 필요 없음
    initial = -alp - cop
    costs = [list(range(tmp, max_cop + tmp + 1)) for tmp in range(initial, initial + max_alp + 1)]
    for idx, cst in enumerate(costs):
        print(idx, ':', cst)

    for i in range(alp, max_alp + 1):
        for j in range(cop, max_cop + 1):

            # 방법1에서만 필요한 부분/ 방법2에서는 필요 x
            # if i < max_alp:
            #     costs[i+1][j] = min(costs[i][j] + 1, costs[i+1][j])
            # if j < max_cop:
            #     costs[i][j+1] = min(costs[i][j] + 1, costs[i][j+1])

            # for idx, cst in enumerate(costs):
            #     print(idx, ':', cst)

            for prob in problems:
                alp_req, cop_req, alp_rwd, cop_rwd, cost = prob
                if alp_req <= i and cop_req <= j:
                    ni, nj = min(i + alp_rwd, max_alp), min(j + cop_rwd, max_cop)
                    costs[ni][nj] = min(costs[i][j] + cost, costs[ni][nj])

    answer = costs[max_alp][max_cop]
    return answer


# case1
# alp, cop = 10, 10
# problems = [[10, 15, 2, 1, 2], [20, 20, 3, 3, 4]]
# case2
alp, cop = 0, 0
problems = [[0, 0, 2, 1, 2], [4, 5, 3, 1, 2], [4, 11, 4, 0, 2], [10, 4, 0, 4, 2]]
print(solution(alp, cop, problems))
