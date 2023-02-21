import sys
sys.stdin = open("input.txt")

n = int(input())
stack = []
numbers = [i for i in range(1, n + 1)]

target = int(input())
i = 1
while i != target:
    stack.append(numbers.pop(0))
    i += 1

