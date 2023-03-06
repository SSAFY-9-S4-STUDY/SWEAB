t = int(input())
for tc in range(1, t + 1):
    n = int(input())  # len(수열)
    arr = list(map(int, input().split()))
    
    ans = -1
    
    for i in range(n - 1):
        for j in range(i + 1, n):
            tmp = arr[i] * arr[j]
            if tmp > 11:  # 11 보다 커야지 수열 성립
                digit = tmp % 10
                tmp //= 10
                while tmp != 0:
                    if digit >= tmp % 10:  # 역순으로 검사하는거라 직전 자릿수가 더 크거나 같아야 함.
                        digit = tmp % 10
                        tmp //= 10
                    else:
                        break
                else:  # 위의 while 제대로 돌았으면
                    ans = max(ans, arr[i] * arr[j])
    
    print(f"#{tc} {ans}")
