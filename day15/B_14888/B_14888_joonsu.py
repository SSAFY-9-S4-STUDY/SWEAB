# 늦어서 죄송합니다 ㅜㅜㅜ
import math

def DFS(idx, result, sum1, sub, mul, div):
    global max_r
    global min_r

    if idx == N:
        max_r = max(max_r, result)
        min_r = min(min_r, result)
        return

    if sum1:
        DFS(idx+1, result+lst[idx], sum1-1, sub, mul, div)
    if sub:
        DFS(idx+1, result-lst[idx], sum1, sub-1, mul, div)
    if mul:
        DFS(idx+1, result*lst[idx], sum1, sub, mul-1, div)
    if div:
        if result < 0:
            new_r = -1*(-1*result // lst[idx])
        else:
            new_r = result // lst[idx]
        DFS(idx+1, new_r, sum1, sub, mul, div-1)

N = int(input())
lst = list(map(int, input().split()))
sum1, sub, mul, div = map(int, input().split())
max_r = -math.inf
min_r = math.inf

DFS(1, lst[0], sum1, sub, mul, div)
print(max_r)
print(min_r)