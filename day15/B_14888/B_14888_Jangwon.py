def calculate(tool, numbers):
    if tool == '+':
        return numbers.pop() + numbers.pop()

    if tool == '-':
        return numbers.pop() - numbers.pop()

    if tool == '*':
        return numbers.pop() * numbers.pop()

    if tool == '/':
        a = numbers.pop()
        b = numbers.pop()
        if a < 0:
            return -(abs(a) // b)
        else:
            return a // b


def dfs(depth):
    global answers
    if depth == N - 1:
        numbers = n_lst[:]
        for t in sel:
            numbers.append(calculate(t, numbers))
        answers.append(numbers[0])
        return

    for k in range(len(tmp)):
       if not visited[k]:
            visited[k] = 1
            sel[depth] = tmp[k]
            dfs(depth + 1)
            visited[k] = 0


N = int(input())
# 숫자들(해당 리스트를 스택처럼 생각)
n_lst = list(map(int, input().split()))
n_lst.reverse()

# 연산자 갯수(+, -, *, /)
tools = list(map(int, input().split()))
tmp = ''
for k in range(4):
    if tools[k]:
        if k == 0:
            tmp += '+' * tools[k]
        elif k == 1:
            tmp += '-' * tools[k]
        elif k == 2:
            tmp += '*' * tools[k]
        else:
            tmp += '/' * tools[k]

visited = [0 for _ in range(len(tmp))]
sel = [0 for _ in range(len(tmp))]
# 정답받는 곳
answers = list()
dfs(0)
answers.sort()
print(answers[-1])
print(answers[0])