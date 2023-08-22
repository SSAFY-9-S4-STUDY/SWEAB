def solution(n, m, x, y, queries):
    answer = -1
    # 공이 한번에 움직인다고 생각
    # 공의 범위를 사각형으로 두고 생각
    x_max, x_min, y_max, y_min = x,x,y,y
    # 역순
    queries.reverse()
    for role, dx in queries:
        if role == 0:
            y_max += dx
            
            if y_max >= m:
                y_max = m - 1
            if y_min != 0:
                y_min += dx
        
        elif role == 1:
            y_min -= dx

            if y_min < 0:
                y_min = 0
            if y_max != m - 1:
                y_max -= dx
        
        elif role == 2:
            x_max += dx

            if x_max >= n:
                x_max = n - 1
            if x_min != 0:
                x_min += dx

        elif role == 3:
            x_min -= dx
            
            if x_min < 0:
                x_min = 0

            if x_max != n-1:
                x_max -= dx
        
        # 범위 벗어나면 공이 없다
        if x_min > n or x_max < 0 or y_min > m or y_max < 0:
            return 0
        else:
            answer = (x_max - x_min + 1) * (y_max - y_min + 1)

    return answer