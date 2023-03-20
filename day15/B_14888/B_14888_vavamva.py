# 연산자 끼워넣기
import itertools


def calc(a, sign_, b):
    if sign_ == 'plus':
        return a + b
    elif sign_ == 'minus':
        return a - b
    elif sign_ == 'multi':
        return a * b
    else:  # b는 무조건 0보다 크다.
        if a >= 0:
            return a // b
        else:
            return (abs(a) // b) * (-1)


def calculator(arr, cal_):
    cal_ = [*cal_]
    quest = arr.copy()
    while len(quest) > 1:
        pre = quest.pop(0)
        post = quest.pop(0)
        sign_ = cal_.pop(0)
        quest.insert(0, calc(pre, sign_, post))

    return quest[0]


n = int(input())
numbers = list(map(int, input().split()))
plus, minus, multi, div = map(int, input().split())

cal = ['minus'] * minus + ['div'] * div + ['plus'] * plus + ['multi'] * multi

result_max = (-1) * (100 ** 11)
result_min = 100 ** 11

no_duple = set(itertools.permutations(cal))

for operator in no_duple:
    tmp = calculator(numbers, operator)
    if tmp < result_min:
        result_min = tmp
    if tmp > result_max:
        result_max = tmp

print(result_max)
print(result_min)

