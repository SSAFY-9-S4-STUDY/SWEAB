N, K = map(int, input().split())
items = sorted([tuple(map(int, input().split())) for _ in range(N)])

values, weights= [0]*(K+1), set()

for i in items:
    for j in range(K,i[0]-1,-1):
        tmp_v = values[j-i[0]]+i[1]
        values[j] = max(values[j], tmp_v)
    
print(max(values))
