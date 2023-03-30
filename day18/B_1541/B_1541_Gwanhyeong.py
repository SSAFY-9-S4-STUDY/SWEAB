from collections import deque
# 입력을 디큐로 받음
arr = deque(input())
# 출력할 답을 ans 변수에 할당
ans = 0

# 숫자를 넣어 놓을 변수 tmp
tmp = ''

# '-'가 한번도 안 나온 경우 convert = False
# '-' 한번이라도 나오면 convert = True
# True 인 경우 사칙연산이 나오면 ans 에서 tmp 를 빼기만 해줌
convert = False
while arr:
    check = arr.popleft()
    if check == '-':
        if convert:
            ans -= int(tmp)
        else:
            ans += int(tmp)
            convert = True
        tmp = ''
    elif check == '+':
        if convert:
            ans -= int(tmp)
        else:
            ans += int(tmp)
        tmp = ''
    else:
        tmp += check

if convert:
    ans -= int(tmp)
else:
    ans += int(tmp)
print(ans)
