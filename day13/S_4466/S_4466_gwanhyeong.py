import sys
sys.stdin = open('sample_input.txt')

# 정렬을 이용한 풀이
t= int(input())
for tc in range(1, t+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    ans = 0
    for i in range(K):
        ans += arr[i]
    
    print(f'#{tc} {ans}')

    