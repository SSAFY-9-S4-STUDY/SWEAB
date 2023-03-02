import sys
sys.stdin = open("sample_input.txt")
for tc in range(1,11):
    V, E = map(int,input().split())

    dictionary = {}
    for i in range(1,V+1):
        dictionary[i] = []
    temp_list = list(map(int,input().split()))
    for i in range(E):
        dictionary[temp_list[i*2+1]].append(temp_list[i*2])

    visited = [0] *(V+1)

    ans = []
    while len(ans) < V:
        for i in range(1,V+1):
            if dictionary[i]==[] and visited[i] == 0:
                ans.append(i)
                visited[i] = 1
                for j in range(1,V+1):
                    if i in dictionary[j]:
                        dictionary[j].remove(i)


    print(f'#{tc}',*ans)