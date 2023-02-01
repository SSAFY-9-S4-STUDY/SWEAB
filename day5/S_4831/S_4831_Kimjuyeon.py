T = int(input())

for j in range(T):
    K, N, M = map(int,input().split())
    lst = list(map(int,input().split()))
    lst.append(N)


    distance = [lst[0],]
    for i in range(M):
        distance.append(lst[i+1]-lst[i])


    distance_after_charge = 0
    result = 0

    for i in range(len(distance)-1):

        if distance[i] > K:
            result = 0
            break
        distance_after_charge += distance[i]
        if distance_after_charge + distance[i+1] > K:
            distance_after_charge = 0
            result += 1
    print(f'#{j+1} {result}')