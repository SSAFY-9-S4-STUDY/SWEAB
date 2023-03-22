# 각 무게마다 최대 가치를 찾고
# 그 중 최대값을 찾는 로직

N, K = map(int, input().split())
items = [(map(int, input().split())) for _ in range(N)]
values = [0]*(K+1)

for w, v in items:
    for i in range(K, w-1, -1):
        values[i] = max(values[i], values[i-w] + v)
    
print(max(values))