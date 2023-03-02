import sys
sys.stdin = open('input.txt', 'r')
from pprint import pprint
T = 10
for test_case in range(1, T+1):
    V, E = map(int, input().split())
    lst = list(map(int, input().split()))
    arr = [[] for _ in range(V+1)]
    visited = [0] * (V+1)
    result = []

    for i in range(len(lst)//2):
        node1 = lst[i*2]
        node2 = lst[i*2+1]
        arr[node2].append(node1)

    while len(result) != V:
        for i in range(1, len(arr)):
            if not visited[i]:
                for j in arr[i]:
                    if not visited[j]:
                        break
                else:
                    visited[i] = 1
                    result.append(i)

    print(f'#{test_case}', *result)