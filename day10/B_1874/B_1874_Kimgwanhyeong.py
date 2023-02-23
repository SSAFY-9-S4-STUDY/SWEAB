n = int(input())

visited = [0] * (n+1)
now = 0
result = []
for _ in range(n):
    next = int(input())

    if next < now:
        if 0 in visited[next+1:now]:
            print('NO')
            break
        else:
            missing = visited[next+1:now].count(1)
            for _ in range(now-next-missing):
                result.append('-')
            visited[next] = 1
            now = next
    elif next > now:
        missing = visited[now+1:next].count(1)
        for _ in range(next - now - missing):
            result.append('+')
        result.append('-')
        visited[next] = 1
        now = next

else:
    for char in result:
        print(char)
