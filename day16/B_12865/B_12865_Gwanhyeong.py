import sys
input = sys.stdin.readline
N, K = map(int, input().split())

bag = [0] * (K+1)
for _ in range(N):
    weight, value = map(int, input().split())
    for i in range(K, weight-1, -1):
        bag[i] = max(bag[i], bag[i-weight] + value)

print(bag[-1])