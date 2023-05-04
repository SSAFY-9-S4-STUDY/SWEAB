from collections import deque

def solution(rectangles, cx, cy, ix, iy):
    # 배열에 사각형 표시하기
    arr = [[0]*102 for _ in range(102)]
    for x1, y1, x2, y2 in rectangles:
        for y in range(y1, y2):
            for x in range(x1, x2):
                arr[2*y][2*x] = 1
    # x,y가 짝수 = 사각형
    # x,y가 홀수 = 캐릭터가 이동하는 줄
    cx, cy, ix, iy = 2*cx-1, 2*cy-1, 2*ix-1, 2*iy-1
    # 출발지를 큐에 넣어서 도착지까지의 최단거리를 측정
    queue  = deque([(cx, cy, 0)])
    arr[cy][cx] = 1
    while queue:
        x, y, cnt = queue.popleft()
        # 만약 도착지점이면 cnt를 반환
        if x == ix and y == iy:
            return cnt
        # 현재 위치에서 기록된 사각형 탐색
        # m: 감소, p: 증가
        mxmy, mxpy, pxpy, pxmy = arr[y-1][x-1], arr[y+1][x-1], arr[y+1][x+1], arr[y-1][x+1]
        # 이동할 때 정면 방향으로 기록된 사각형이 한쪽은 있고 한쪽은 없어야 이동
        # x 증가 방향 이동
        if [pxpy, pxmy].count(1) == 1 and not arr[y][x+2]: 
            queue.append((x+2, y, cnt+1))
            arr[y][x+2] = 1
        # x 감소 방향 이동
        if [mxpy, mxmy].count(1) == 1 and not arr[y][x-2]: 
            queue.append((x-2, y, cnt+1))
            arr[y][x-2] = 1
        # y 증가 방향 이동
        if [pxpy, mxpy].count(1) == 1 and not arr[y+2][x]: 
            queue.append((x, y+2, cnt+1))
            arr[y+2][x] = 1
        # y 감소 방향 이동
        if [pxmy, mxmy].count(1) == 1 and not arr[y-2][x]: 
            queue.append((x, y-2, cnt+1))
            arr[y-2][x] = 1