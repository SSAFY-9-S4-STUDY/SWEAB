# 30점 짜리 답안...
# 주어진 4개 테스트 케이스는 맞았으나, 이후 틀렸습니다, 시간 초과 등등 여러 문제 존재

def solution(n, paths, gates, summits):
    adj_L = [[] for _ in range(n+1)]
    for path in paths:
        adj_L[path[0]].append((path[1],path[2]))
        adj_L[path[1]].append((path[0],path[2]))

    def dfs(node, intensity):
        nonlocal tmp_int, tmp_summit
        if node in summits:
            if intensity < tmp_int:
                tmp_int = intensity
                tmp_summit = node
            elif intensity == tmp_int:
                tmp_summit = min(tmp_summit,node)
            return
        for next, w in adj_L[node]:
            if visited[next] == 0:
                visited[next] = 1
                dfs(next, max(w, intensity))
                visited[next] = 0

    tmp_int = 1e7
    tmp_summit = 0
    for start in gates:
        visited = [0] * (n+1)
        visited[start] = 1
        dfs(start, 0)
    answer = [tmp_summit, tmp_int]
    return answer