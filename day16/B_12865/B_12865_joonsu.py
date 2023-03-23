N, K = map(int, input().split())
queue = [(0,0)]
arr = [[0] * (K+1) for _ in range(N+1)]

for _ in range(N):
    W, V = map(int, input().split())
    queue.append((W, V))
    # print(queue)

for i in range(1, N+1):
    for j in range(1, K+1):
        W = queue[i][0]
        V = queue[i][1]
        if j < W:
            arr[i][j] = arr[i-1][j]
        else:
            arr[i][j] = max(arr[i-1][j], V+arr[i-1][j-W])

print(arr[N][K])

'''             
dp[i][j] = max(현재 물건 가치 + dp[이전 물건][현재 가방 무게 - 현재 물건 무게],
                dp[이전 물건][현재 가방 무게])
'''