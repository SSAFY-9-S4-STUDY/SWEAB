for tc in range(1,11):
    V, E = map(int,input().split())
    temp = list(map(int,input().strip().split()))
    
    info = [[] for _ in range(V+1)]
    for i in range(E):
        info[temp[2*i+1]].append(temp[2*i])
    # 자식 노드 인덱스로 부모 노드 저장하는 것과 같은 방식으로 자료 저장

    arr = ''
    visited = [0] *(V+1)
    while True:
        if sum(visited) == V:
            break
        for k in range(1, V+1):
            if info[k] == [] and not visited[k]:
                arr += f' {k}' 
                visited [k] = 1
                for i in info:
                    if k in i:
                        i.remove(k)

    print(f'#{tc}{arr}')