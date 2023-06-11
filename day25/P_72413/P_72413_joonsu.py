def solution(n, s, a, b, fares):
    arr = [[100000] * n for _ in range(n)]
    answer = 100000

    for i in range(n):
        for j in range(n):
            if i == j:
                arr[i][j] = 0

    for i in fares:
        node1, node2, f = i
        arr[node1 - 1][node2 - 1] = f
        arr[node2 - 1][node1 - 1] = f

    for k in range(n):
        for i in range(n):
            for j in range(n):
                arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

    for i in range(n):
        temp = arr[s-1][i] + arr[i][a-1] + arr[i][b-1]
        answer = min(temp, answer)

    return answer