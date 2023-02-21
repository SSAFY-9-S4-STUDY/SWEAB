import sys

N, M, K = map(int, sys.stdin.readline().split())
sr = [[0 for _ in range(M + 1)] for _ in range(N+1)]
ans = K ** 2

for i in range(N):
    a = sys.stdin.readline().rstrip()
    for j in range(M):
        sr[i + 1][j + 1] = (((i + j) % 2 == 0) ^ (a[j] == 'W')) + sr[i][j + 1] + sr[i + 1][j] - sr[i][j]

ans = []
for i in range(K - 1, N):
    for j in range(K - 1, M):
        ans.append(sr[i + 1][j + 1] - sr[i + 1][j - K + 1] - sr[i - K + 1][j + 1] + sr[i - K + 1][j - K + 1])

print(min(K ** 2 -max(ans), min(ans)))

'''
주어진 나무 판자를 lst에 받아오려고 했으나 더 효율적인 코드를 위해서 생략
한 줄씩 직접 읽으면서 누적합 arr에 적용해나갔습니다.

마지막에 min(K ** 2 - temp, temp, ans)를 했었지만 연산이 많아 시간초과
ans 리스트에 넣어서 max와 min을 한 번에 처리해 연산수를 줄였습니다.(이부분 인터넷 참조)

시간 줄이기 2가지 팁
1. pypy 사용하기
2. 코드 전체를 main() 함수 내부에 저장하고 return값 설정
마지막 부분에 
if __name__ == '__main__':
    print(main())
이거 하면 시간초과가 줄어든다. 교수님도 왜그런지 모름. 원래는 더 느려야하는데... 이상한 백주니

'''