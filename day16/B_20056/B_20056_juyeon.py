from collections import defaultdict
import copy

dir_dixt = {
    0:(-1, 0), 1:(-1, 1), 2:(0, 1), 3:(1, 1), 4:(1, 0), 5:(1, -1), 6:(0, -1), 7:(-1, -1), 
}

N, M, K = map(int, input().split())
balls = [[]for _ in range(M)]
for i in range(M):
    ball = list(map(int, input().split()))
    ball[0] -=1
    ball[1] -=1
    balls[i] = ball # r, c, m, s, d

for i in range(K):
    if not balls:
        break
    
    temp_dic = defaultdict(list)
    for ball in balls:

        idx_i, idx_j = dir_dixt[ball[4]]
        ball[0] += idx_i*ball[3]
        ball[0] %= N 
        ball[1] += idx_j*ball[3]
        ball[1] %= N
        temp_dic[(ball[0], ball[1])].append([ball[2], ball[3], ball[4]])
    
    balls = []
    for pos, info in temp_dic.items():
        if len(info) > 1:
            new_m = sum(list(zip(*info))[0]) // 5
            if new_m:
                new_s = sum(list(zip(*info))[1]) // len(info)
                t = -1
                for k in list(zip(*info))[2]:
                    idx = k % 2
                    if t != -1 and idx != t:
                        new_d = [1,3,5,7]
                        break
                    t = idx 
                else:
                    new_d = [0,2,4,6]
        else:
            balls.append([*pos,info[0][0], info[0][1], info[0][2]])
            continue
        if new_m:
            for i in new_d:
                balls.append([pos[0], pos[1], new_m, new_s, i])

if balls:
    print(sum(list(zip(*balls))[2]))
else:
    print('0')