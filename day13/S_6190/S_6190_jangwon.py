T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    num_lst = list(map(int, input().split()))
    num_lst.sort(reverse=True)
    ans = -1
    for i in range(N - 1):
        for j in range(i + 1, N):
            tmp = num_lst[i] * num_lst[j]
            if tmp < ans:
                break
            else:
                if str(tmp) == ''.join(sorted(str(tmp))):
                    if ans < tmp:
                        ans = tmp

    print(f'#{test_case} {ans}')