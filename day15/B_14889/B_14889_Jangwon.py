def dfs(point, depth):
    global ans
    # 팀이 다 나뉘어졌다면, 판단 시작
    if depth == N / 2:
        start = link = 0
        for i in range(N):
            for j in range(i + 1, N):
                # visited를 쭉 보면서 1로 같은 거끼리 한 팀, 아닌 거끼리 한팀.
                if visited[i] and visited[j]:
                    start += arr[i][j] + arr[j][i]
                elif not visited[i] and not visited[j]:
                    link += arr[i][j] + arr[j][i]
        ans = min(ans, abs(start - link))
        return

    # 이 부분 백트랙킹 생각을 잘 못해서 구글의 힘을 조금 받았습니당....
    # 혼자 계속 set을 쓰고 뻘짓을 했는데 간단하게 할 수 있을 거 같다는 생각이 들어군용
    for k in range(point, N):
        if not visited[k]:
            visited[k] = 1
            dfs(k + 1, depth + 1)
            visited[k] = 0

N = int(input())

arr = [list(map(int, input().split())) for _  in range(N)]

visited = [0 for _ in range(N + 1)]
ans = 987654321
dfs(0, 0)
print(ans)