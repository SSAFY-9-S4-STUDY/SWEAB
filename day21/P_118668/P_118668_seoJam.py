def solution(alp, cop, problems):
    answer = 0

    max_alp = max_cop = 0
    for problem in problems:
        max_alp = max(max_alp, problem[0])
        max_cop = max(max_cop, problem[1])

    dp = list([i + j for i in range(max_alp+1)] for j in range(max_cop+1))


    return answer


print(solution(10, 10, [[10,15,2,1,2],[20,20,3,3,4]]))