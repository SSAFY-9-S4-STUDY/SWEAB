def solution(numbers):
    # 각 숫자들 사이의 가중치를 미리 계산
    xy = [(3,1)] + [(i // 3, i % 3) for i in range(9)]
    w = [[0]*10 for i in range(10)]
    for s in range(10):
        for e in range(10):
            dr, dc = abs(xy[s][0] - xy[e][0]), abs(xy[s][1] - xy[e][1])
            w[s][e] = dr + dc + max(dr,dc)
    # 초기값은 모든 버튼을 오른손으로 눌렀다고 가정
    N, num = len(numbers), list(map(int,"6" + numbers))
    cum_w = [w[int(num[i])][int(num[i+1])] for i in range(N)]
    for i in range(1, N):
        cum_w[i] += cum_w[i-1]
    # 언제 손을 바꿨을 때 이득인지 기록
    ans, oppose = cum_w[-1], 4
    for i in range(1, N+1):
        tmp = w[oppose][num[i]] + cum_w[-1] - cum_w[i-1]
        if tmp < ans:
            print(tmp)
            ans, oppose = tmp, num[i-1]

    return num, cum_w

print(solution("1756"))