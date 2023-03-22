# 구글은 내 친구

n, limit = map(int, input().split())

# bag의 행: limit + 1 (제한 무게 + 패딩), bag의 열: n + 1 (가능한 짐의 수 + 패딩)
bag = [[0 for _ in range(limit + 1)] for _ in range(n + 1)]

stuff = [[0,0]]  # 사람의 숫자로 바꿔주기 위한 패딩
for _ in range(n):
    stuff.append(list(map(int, input().split())))

#냅색 문제 풀이
for i in range(1, n + 1):
    for j in range(1, limit + 1):
        weight = stuff[i][0] 
        value = stuff[i][1]
       
        if j < weight:  # 들고있는 무게가 weight(넣을 무게)보다 작으면 바로 [이전물건][같은무게] 입력
            bag[i][j] = bag[i - 1][j] 
        else:  # 현재 물건 + 남은 무게를 채울 수 있는 최댓값인, 위의 행에서 가져온 것 vs 다른 물건들로 채운 값 중 큰 값.
            bag[i][j] = max(value + bag[i - 1][j - weight], bag[i - 1][j])

print(bag[n][limit])