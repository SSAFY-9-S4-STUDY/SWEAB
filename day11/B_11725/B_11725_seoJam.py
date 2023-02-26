import sys
input = sys.stdin.readline
sys.stdin = open("sample_input.txt")
from collections import deque

# temp 저장된 각 간선의 연결 정보 중 노드번호 1이 포함된 정보에 대해서
# 1번 노드를 루트로 지정하고, 방문 처리,
# 다른 하나는 child 노드로 지정하고 똑같이 방문처리

# 이후 방문 처리된 노드는 루트로 지정하고,
# 다른 하나는 child 노드로 지정하고 방문처리

N = int(input())
temp = []
visited = [0] * N
ans = []   # 각 idx에 해당하는 노드의 부모노드를 저장

for _ in range(N - 1):
    n1, n2 = map(int, input().split())
    temp.append([n1, n2])

for n1, n2 in temp:
    if 1 in [n1, n2]:
        if n1 == 1:
            ans[n2] = n1
        else:
            ans[n1] = n2
        visited[n1], visited[n2] = 1, 1

while q:



for i in range(2, N + 1):
    print(tree[i])