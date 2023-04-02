# 잃어버린 괄호

def make_int(str_num):
    for i in range(len(str_num)):
        if str_num[i] != '0':
            result = ''.join(str_num[i:])
            return int(result)


quest = input()
operator = []
tmp = []
num = []
for digit in quest:
    if digit == '-' or digit == '+':
        operator.append(digit)
        num.append(make_int(tmp))
        tmp = []
    else:
        tmp.append(digit)
num.append(make_int(tmp))

idx = 0
while idx < len(operator):
    if operator[idx] == '+':
        num[idx + 1] = num[idx] + num[idx + 1]
        num[idx] = 0
    idx += 1

n = len(num)
for i in range(n - 1, -1, -1):
    if num[i] == 0:
        num.pop(i)

idx = 0
num_idx = 0

while len(num) > 1:
    tmp_1 = num.pop(0)
    tmp_2 = num.pop(0)
    num.insert(0, tmp_1 - tmp_2)

print(num[0])