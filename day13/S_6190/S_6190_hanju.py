import sys
sys.stdin = open('6190.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))

    ans = -1
    for i in range(N-1):
        for j in range(i+1,N):
            tmp = str(A[i] * A[j])

            if int(tmp) <= ans:
                continue

            for k in range(len(tmp)-1):
                if int(tmp[k]) > int(tmp[k+1]):
                    break
            else:
                ans = max(ans, int(tmp))

    print(f'#{test_case} {ans}')