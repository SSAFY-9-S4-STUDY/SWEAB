def solution(n, build_frame):
    wall = []

    for [x, y, obj, build] in build_frame:
        
        if build: 
            wall.append([x, y, obj])  # 설치
        else: 
            wall.remove([x, y, obj])  # 제거

        flag = False

        # 설치 or 제거 후 구조물 상태 확인
        for [wx, wy, _] in wall:
            if wx < x - 1 or wx > x + 1 or  wy < y -1 or wy > y + 1:
                continue
            if obj == 0:
                if y == 0 or [wx - 1, wy, 1] in wall or [wx, wy, 1] in wall or [wx, wy - 1, 0] in wall:
                    flag= True
                    break
            else:
                if [wx, wy - 1, 0] in wall or [wx + 1, wy - 1, 0] in wall or ([wx - 1, y, 1] in wall and [wx + 1, y, 1] in wall):
                  flag = True
                  break
        print(flag)
        if flag == False:
            if build: wall.pop()
            else: wall.append([x, y, obj])


    return wall.sort()



print(solution(5,	[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))