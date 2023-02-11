# 재귀함수를 이용해 조합을 구하는 방법...시간초과
# def comb(arr, n):
#     comb_lst = list()
#     if n > len(arr):
#         return comb_lst
#     elif n == 0:
#         comb_lst.append([])
#     elif n == 1:
#         for num in arr:
#             comb_lst.append([num])
    
#     elif n > 1:
#         for i in range(len(arr)-n+1):
#             for j in comb(arr[i+1:], n-1):
#                 comb_lst.append([arr[i]] + j)

#     return 

# 직접 계산하는 방법
t= int(input())
for _ in range(t):
    N, M = map(int,input().split())

    com = 1

    for i in range(M,M-N,-1):
        com *= i
    for j in range(1,N+1):
        com //= j 
    print(com)

# itertools 를 통해 구하는 방법
# from itertools import combinations
# N, K = map(int,input().split())
# cnts=0
# for _ in combinations(range(K),N):
#     cnts+=1
# print(len(comb(range(K),N)))