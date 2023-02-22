N = int(input())
lst = [tuple(map(int, input().split())) for _ in range(N)]
lst = sorted(lst, key=lambda x: (x[1], x[0]))
count = 0
end = 0

for time_s, time_e in lst:
    if time_s >= end:
        end = time_e
        count += 1

print(count)