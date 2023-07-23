def solution(n, m, x, y, queries):
    # 뒤에서부터 따지면서 가능한 시작점 범위 찾기
    sr, sc = x, y
    er, ec = x, y

    for direction, dx in reversed(queries):
        if sr > er or sc > ec:
            return 0
        
        if direction == 0:
            ec = min(m-1, ec+dx)
            sc = sc+dx if sc else sc
            # sc =  min(m-1, sc+dx) if sc else sc
                
        elif direction == 1:
            sc = max(0, sc-dx)
            ec = ec if ec == m-1 else ec-dx
                
        elif direction == 2:
            er = min(n-1, er+dx)
            sr = sr+dx if sr else sr
                
        else:
            sr = max(0, sr-dx)
            er = er if er == n-1 else er-dx
                
    return (er-sr+1)*(ec-sc+1)

print(solution(2,2,0,0,	[[2,1],[0,1],[1,1],[0,1],[2,1]]))
print(solution(2,5,0,1,	[[3,1],[2,2],[1,1],[2,3],[0,1],[2,1]]))