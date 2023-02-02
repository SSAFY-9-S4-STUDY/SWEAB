T = int(input())
for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())
    stations = list(map(int, input().split()))

    charge = [0] * (N+1)
    for i in stations:
        charge[i] = 1

    count = 0
    location = 0
    while location < N - K:
        for move in range(K, -1, -1):
            if not move:
                count = 0
                location = N
                break
            if charge[location + move]:
                count += 1
                location += move
                break

    print(f'#{test_case} {count}')