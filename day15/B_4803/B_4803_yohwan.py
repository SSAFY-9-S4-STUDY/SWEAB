import sys
sys.stdin = open("sample.txt")

# 아직 미완성 임니다...
# 거의 다 푼 것 같은데 자꾸 에러떠요
# 빨리 고쳐볼게요 ㅠㅠ

def tree(start):
    queue = [start]
    res = 1
    while queue:
        x = queue.pop(0)
        if visited[x] == 1:
            res = 0
        else:
            visited[x] = 1
            for y in graph[x]:
                if visited[y] == 1:
                    res = 0
                if visited[y] == 0:
                    queue.append(y)
    return res


tc = 0
n, m = map(int, input().split())
for _ in range(m):
    a, b = map(int, input().split())

    cnt = 0
    graph = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    if n > 0 and m > 0:
        graph[a].append(b)
        graph[b].append(a)

        for i in range(n+1):
            if visited[i] == 0:
                if tree(i) == 1:
                    cnt += 1
            else:
                continue






