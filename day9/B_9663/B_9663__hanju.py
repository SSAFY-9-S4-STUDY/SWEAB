def nqueen(arr, cnt, n):
    if not arr:
        return 0

    if cnt == n-1:
        return 1

    answer = 0
    while arr and arr[0][0] == cnt:

        x, y, c1, c2 = arr.pop(0)
        tmp = []
        for i in arr:
            if i[0] != x and i[1] != y and i[2] != c1 and i[3] != c2:
                tmp.append(i)
        answer += nqueen(tmp, cnt+1, n)

    return answer


N = int(input())
chess = [(j, i, N + i - j - 1, i + j) for j in range(N) for i in range(N)]

print(nqueen(chess,0,N))



