# idea : A 와 B 중 긴 걸 비교해서 긴 리스트를 long에 짧은 리스트를 short에
# 넣은 함수를 정의
def calculate(long, short, arr_long,arr_short):
    ans = 0
    for i in range(long - short +1):
        cnt = 0
        for j in range(short):
            cnt += arr_long[i+j] * arr_short[j]
        if cnt > ans:
            ans = cnt
    return ans


import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1,t+1):
    N, M = map(int, input().split())
    A_list = list(map(int, input().split()))
    B_list = list(map(int, input().split()))
    if N >= M:
        print(f'#{tc} {calculate(N,M,A_list,B_list)}')
    else:
        print(f'#{tc} {calculate(M,N,B_list,A_list)}')
