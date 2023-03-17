from itertools import permutations

def operation(a, b, op):
    if op == "+":
        return a+b
    elif op == "-":
        return a-b
    elif op == "*":
        return a*b
    else:
        if a >= 0:
            return a//b
        if a < 0:
            return abs(a)//b*(-1)


N = int(input())
numbers = list(map(int,input().split()))
ops = []
for i,j in zip(["+","-","*","/"],map(int,input().split())):
    for k in range(j):
        ops.append(i)

ans = []
for perm in set(permutations(ops,N-1)):
    number = numbers[0]
    for n,op in zip(numbers[1:],perm):
        number = operation(number,n,op)
    ans.append(number)

print(max(ans))
print(min(ans))