# SWEA 2001

# 파리 덫 매핑 (Input 을 N*N 행렬로 만들기)
def flymap_ing(N):
    fly_map= []
    for i in range (N):
        fly_map.append(list(map(int,input().split())))
    return fly_map

# (x, y) 왼쪽 위 끝점으로 가지는 M*M 행렬 합
def calculator(list:list, M, x, y):
    N = len(list)
    fin_list = []
    for j in range (x, x+M):
        a = []
        for i in range (y, y+M):
            a.append(list[j][i])
        fin_list.append(a)
    result = sum(sum(fin_list,[]))
    return result

T= int(input())

for i in range (T):
    N , M = map(int,input().split())

    fly_map = flymap_ing(N)
    sum_max = fly_map[0][0]
    for x in range(N-M+1):
        for y in range(N-M+1):
            a = calculator(fly_map, M, x, y)
            if a > sum_max: sum_max = a


    print(f'#{i+1} {sum_max}')