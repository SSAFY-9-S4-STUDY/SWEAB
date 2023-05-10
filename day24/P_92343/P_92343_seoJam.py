def solution(info, edges):
    global answer
    answer = 0
    visited = [0] * len(info)
    visited[0] = 1

    def dfs(sheeps, wolves):
        global answer
        # 늑대가 양보다 많을 때
        if sheeps <= wolves:
            return
        # 다음 노드로 이동
        for parent, child in edges:
            if visited[parent] and not visited[child]:
                visited[child] = 1
                dfs(sheeps + (not info[child]), wolves + info[child])
                visited[child] = 0
        # 양 최대값 갱신
        answer = max(answer, sheeps)

    dfs(1, 0)

    return answer

