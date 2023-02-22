# 코드 최적화 필요함. 너무 복잡하게 푼듯.... ㅜ.ㅜ
N = int(input())
sample = [0] * N
for i in range(N):
    sample[i] = int(input())

stack = []
idx = 0
res = ''
numbers = list(range(1, N+1))
sample2 = [0] * N
for i in numbers:
    if not stack:
        stack.append(i)
        res += '+'
    elif stack and sample[idx] != stack[-1]:
        stack.append(i)
        res += '+'
    else:
        while stack and sample[idx] == stack[-1]:
            sample2[idx] = stack.pop()
            res += '-'
            
            idx += 1
            
        if idx < N:
            stack.append(i)
            res += '+'

while stack:
    sample2[idx] = stack.pop()
    res += '-'
    idx += 1
if sample2 != sample:
    print('NO')
else:
    for i in res:
        print(i)