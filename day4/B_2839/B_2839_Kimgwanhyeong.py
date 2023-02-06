n = int(input())
trial = 0
x = 0
y = 0
while 5 * trial <= n:
    if (n - 5 * trial) % 3 == 0:
        x = trial
        y = (n - 5 * trial) // 3

    trial += 1



if 5 * x + 3 * y != n:
    print(-1)
else:
    print(x+y)
