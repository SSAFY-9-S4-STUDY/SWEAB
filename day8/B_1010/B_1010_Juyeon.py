# nCk 를 구하는 함수 
# 이용한 성질 = nCk = (n-1)Ck + (n-1)C(k-1)
def fac_list(N,K):
    res = [[0]*(N+1) for _ in range(K+1)]
    for j in range(N+1):
        res[0][j] = 1
    for i in range(K+1):
        res[i][i] = 1

    for i in range(1, K+1):
        for j in range(i+1, N+1):
            res[i][j] = res[i][j-1] + res[i-1][j-1]
    return res

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    res_list = fac_list(M,N)
    res = res_list[N][M] 
    print(res)