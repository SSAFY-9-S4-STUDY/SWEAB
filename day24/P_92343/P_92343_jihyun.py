def solution(info, edges):
    visited = [0] * len(info)
    visited[0] = 1
    answer = 0

    def dfs(sheep_cnt, wolf_cnt):
        nonlocal answer

        if sheep_cnt <= wolf_cnt:
            return
        
        answer = max(sheep_cnt, answer)

        for p, c in edges:
            if visited[p] and not visited[c]:
                visited[c] = 1
                if info[c] == 0:
                    dfs(sheep_cnt+1, wolf_cnt)
                else:
                    dfs(sheep_cnt, wolf_cnt+1)
                visited[c] = 0
    
    dfs(1, 0)

    return answer



info1 = [0,0,1,1,1,0,1,0,1,0,1,1]
edges1 = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
print('#1', solution(info1, edges1))

info2 = [0,1,0,1,1,0,1,0,0,1,0]
edges2 = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]
print('#2', solution(info2, edges2))
