# [1] 입력된 수열 값 > i 이면 같아질때 까지 push
# [2] 이후 스택 마지막 값 pop
# [3] 스택 마지막 값과 입력된 수열값이 같다면 pop
# [3-1] 스택값과 수열값이 서로 다르면 가망 없음. break
# [4] 새로운 수열값 입력 받아서 [1]~[3] 반복 
# [5] break 없이 for문이 끝나면 ans 출력

n = int(input())
stack = []
ans = []    # ans: 최종 출력 리스트

i = 1   # i: 1부터 n까지의 수

for _ in range(n):
    # 수열 입력 받기
    series = int(input())

    # i가 수열값보다 작으면?
    if i <= series:
        while i <= series:   # i랑 같아질 때 까지
            stack.append(i)  # push
            ans.append('+')
            i += 1
    # 이후 스택값과 수열값이 같다면?
    if stack[-1] == series:
        stack.pop()
        ans.append('-')
    # 다르다면?
    else:
        print('NO')   # 'NO' 출력
        break
# for문이 끝나면?
else:
    for token in ans:
        print(token)  # ans 출력