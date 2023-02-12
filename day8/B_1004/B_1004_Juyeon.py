T = int(input())
for tc in range(1, T+1):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    
    # 각 행성 위치를 tuple 로 저장
    planets = [tuple(map(int, input().split())) for _ in range(n)] 
    
    cnt = 0 # 진입/이탈 횟수 저장
    
    # 출발점, 행성의 거리와 행성 반지름 비교, st, fi 에는 True or False 가 저장됨
    for i in planets:
        st = ((i[0]-x1)**2 + (i[1]-y1)**2) < i[2]**2 
        fi = ((i[0]-x2)**2 + (i[1]-y2)**2) < i[2]**2
        temp = (st+ fi) % 2 # (1,0) or (0,1) 일때만 1회 진입 or 이탈을 함
        cnt += temp # 더해줌

    print(cnt)