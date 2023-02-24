import sys
N = int(input())

nodes = [[] for _ in range(N + 1)]
for i in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    nodes[a].append(b)
    nodes[b].append(a)
stk = [0] * (N + 1)
top = -1
top +=1
stk[top] = 1
visited = [0] * (N + 1)
'''
def find_jokbo(node):
    global nodes, ans
    for i in nodes[node]:
        if ans[i] == 0:
            ans[i] = node
            find_jokbo(i)


find_jokbo(1)

재귀는 recursionerror가 뜹니다!!
'''
while top != -1:
    cur = stk[top]
    top -= 1

    for i in nodes[cur]:
        if visited[i] == 0:
            visited[i] = cur
            top += 1
            stk[top] = i

for i in range(2, N + 1):
    print(visited[i])