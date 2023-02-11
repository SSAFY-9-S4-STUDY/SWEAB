# combination 구하는 문제
# itertools 이용도 해보고 재귀함수로도 구현해봤지만...
# 결국 런타임 에러, 시간초과 나서 직접 계산했음.

N, K = map(int,input().split())
com = 1

for i in range(N,N-K,-1):
    com *= i
for j in range(1,K+1):
    com //= j 
print(com % 10007)