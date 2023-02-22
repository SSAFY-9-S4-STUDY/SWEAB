def coloring():
    global sample
    sample = [[0 for _ in range(M+1)]for _ in range(N+1)]
    for i in range(1, N+1):# 일단 바둑판 인덱스 성질 이용해서 숫자로 변환해줌  -> dols= {1:'B', 0:'W'}
        for j in range(1, M+1):
            if board[i-1][j-1] != dols[(i+j) % 2]:
                sample[i][j] += 1

    # 시간 초과떠서 2차원의 누적합을 이용하고자 하였음
    # 먼저 행 누적해줌
    for i in range(1, N+1): 
        for j in range(1,M+1):
            sample[i][j] += sample[i][j-1] 

    #같은 열에서 누적해줌
    for i in range(1, N+1):
        for j in range(1,M+1):
            sample[i][j] += sample[i-1][j]

    
    min_res = K**2 # 초기 최소값 설정. 모든 바둑알을 뒤집을때 나올 수 있는 경우임
    for i in range(K, N+1):
        for j in range(K, M+1):
            temp_sum = sample[i][j]-sample[i-K][j]-sample[i][j-K]+sample[i-K][j-K] # 체스판의 (i-K+1,j-K+1) : 왼쪽위 ~ (i,j) : 오른쪽 아래 까지의 2차원 행렬의 합

            # 최종 나올 수 있는 바둑판이 총 2개인데, 뒤집어야 하는 돌의 수의 합은 K**2 일테니까 이때만 계산해줌
            if min_res > temp_sum:
                min_res = temp_sum
            if min_res > K**2 - temp_sum: 
                min_res = K**2 - temp_sum
    return min_res

N, M, K = map(int,input().split())
board = [input() for _ in range(N)]
dols= {1:'B', 0:'W'}
print(coloring())