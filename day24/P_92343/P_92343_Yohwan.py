def solution(info, edges):
    global answer
    visited = [0] * len(info)
    visited[0] = 1
    answer = 0
    
    def dfs(sheep, wolf):
        global answer
        if sheep > wolf :
            answer = max(sheep, answer)
        else:
            return
        
        for i in range(len(edges)):
            if visited[edges[i][0]] and not visited[edges[i][1]]:
                visited[edges[i][1]] = 1
                if info[edges[i][1]] == 0 :
                    dfs(sheep+1, wolf)
                else:
                    dfs(sheep, wolf+1)
                visited[edges[i][1]] = 0     
                
    dfs(1, 0)
    return answer