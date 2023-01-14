T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    a = map(int, input().split())
    a = list(a)
    a.sort()
    result = a[-1] - a[0]
    print("#" + str(test_case) + ' ' + str(result))