# point가 행성계 안에 있는지 밖에 있는지 확인하는 함수 정의
def is_in_galaxy(p_x, p_y,g_x,g_y,g_r):
    return (p_x - g_x)**2 + (p_y - g_y)**2 < g_r **2


t = int(input())
for _ in range(1, t+1):
    # 시작점의 x,y좌표와 도착점의 x,y좌표를 입력
    start_x, start_y, end_x, end_y = map(int,input().split())
    # 행성계의 개수를 변수에 할당
    galaxy = int(input())
    # 진입/이탈 할 수 밖에 없는 행성계 개수 합 변수에 할당
    cnts = 0
    for i in range(galaxy):
        # 행성계의 x,y 좌표와 반지름 입력
        x, y, r = map(int,input().split())
        # 시작점이 행성계 밖에 있고, 도착점이 행성계 안에 있으면 진입/이탈할 수 밖에
        # 또, 시작점이 행성계 안에 있고, 도착점이 행성계 밖에 있으면 진입/이탈할 수 밖에
        if is_in_galaxy(start_x,start_y,x,y,r) != is_in_galaxy(end_x,end_y,x,y,r):
            cnts += 1
    print(cnts)