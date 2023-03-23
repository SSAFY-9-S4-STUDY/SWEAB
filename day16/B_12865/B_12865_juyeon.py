import sys
sys.setrecursionlimit(10000)

def packing(idx):
    global w, max_value, now_value
    if w > K or idx > N-1:
        return 
    else:
        if now_value > max_value:
            max_value = now_value
        for i in [1,0]:
            if w < K:
                now_value += things[idx][1]*i
                w += things[idx][0]*i
                packing(idx+1)
                now_value -= things[idx][1]*i
                w -= things[idx][0]*i

N, K = map(int,input().split())
things = []
for i in range(N):
    things.append(list(map(int,input().split())))


w = 0
max_value = 0
now_value = 0
packing(0)

print(max_value)

# 시간 초과 떠서 구글링해서 아이디어 참고하여 구현함.ㅜㅜ 또륵 

N, K = map(int,input().split())
things = []
for i in range(N):
    things.append(list(map(int,input().split()))) # W, V
    
values = [[0 for _ in range(K+1)]for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, K+1):
        if things[i-1][0] <= j:
            values[i][j] = max(things[i-1][1]+values[i-1][j-things[i-1][0]], values[i-1][j])
        else:
            values[i][j] = values[i-1][j]

print(values[N][K])