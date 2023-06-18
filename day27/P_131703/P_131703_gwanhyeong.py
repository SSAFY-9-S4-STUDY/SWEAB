def solution(beginning, target):
    answer = 0
    # m: 직사각형의 행 개수, n: 직사각형 열 개수
    m = len(beginning)
    n = len(beginning[0])
    # diff = [[] for _ in range(N)]
    # for i in range(N):
    #     for j in range(N):
    #         diff[i].append(beginning[i][j] ^ target[i][j])

    # 리스트 컴프리헨션
    diff = [[beginning[i][j] ^ target[i][j] for j in range(n)] for i in range(m)]
    # print(diff)
    
    cnt = 0
    # diff 의 첫번째 행을 기준으로 나머지 행이 일치하지 않는다면, 뒤집는다.
    # 뒤집은 결과마저 첫번째 행과 동일하지 않는다면 -1 리턴
    for i in range(1, m):
        if diff[i] != diff[0]:
            cnt += 1
            if (list(map(lambda x: x ^ 1, diff[i])) != diff[0]):
                return -1
    
    # 뒤집은 횟수(행의 개수) + 첫번째 행의 1의 개수가 정답의 후보 중 하나
    # 다른 하나는 첫번째 행을 뒤집었을 때 (행의 크기 - 뒤집은 행의 개수) + (열의 크기 - 첫 번째 행의 1의 개수)
    answer = min((cnt + sum(diff[0]), (m - cnt) + (n - sum(diff[0]))))
    
    return answer

solution([[0, 1, 0, 0, 0], [1, 0, 1, 0, 1], [0, 1, 1, 1, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]],[[0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [0, 0, 1, 0, 1], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]])