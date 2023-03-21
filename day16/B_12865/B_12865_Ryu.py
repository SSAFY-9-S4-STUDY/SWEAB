import sys
input = sys.stdin.readline

N, K = map(int, input().split())
lst = []

for _ in range(N):
    W, V = map(int, input().split())
    lst.append((W, V))

# n**2된다?  빈리스트에서 채우기 옆에 무게 넣어주기 3칸리스트

lst_w = [[] for _ in range(K + 1)]

# 빼는 개념

max_v = 0

for i in range(1, K + 1):
    for j in range(N):
        if i - lst[j][0] == 0:
            if not lst_w[i]:
                lst_w[i].append(j)
                max_v = max(max_v, lst[j][1])
            else:
                total_v = 0
                for yo in lst_w[i]:
                    total_v += lst[yo][1]
                if total_v < lst[j][1]:
                    lst_w[i] = [j]
                max_v = max(total_v, lst[j][1], max_v)
        elif i - lst[j][0] > 0 and lst_w[i -lst[j][0]] and j not in lst_w[i - lst[j][0]]:
            if not lst_w[i]:
                lst_w[i] = lst_w[i -lst[j][0]] + [j]
                total_v1 = 0
                for yo in lst_w[i]:
                    total_v1 += lst[yo][1]
                max_v = max(max_v, total_v1)
            else:
                total_v1 = 0
                for yo in lst_w[i]:
                    total_v1 += lst[yo][1]
                total_v2 = 0
                for yo in lst_w[i - lst[j][0]]:
                    total_v2 += lst[yo][1]
                total_v2 += lst[j][1]
                if total_v1 < total_v2:
                    lst_w[i] = lst_w[i - lst[j][0]] + [j]
                max_v = max(total_v1, total_v2, max_v)

print(max_v)