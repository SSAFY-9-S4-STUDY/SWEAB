# - 한번 나오면 그 이후 숫자 모두 빼면 됨

text = input()
rlt = 0
temp = ''
swi = 0
for i in text:
    if i.isdecimal():
        temp += i
    elif swi == 1 and not i.isdecimal():
        rlt -= int(temp)
        temp = ''
    elif swi == 0 and not i.isdecimal():
        rlt += int(temp)
        temp = ''
        if i == '-':
            swi = 1
if swi == 1:
    rlt -= int(temp)
else :
    rlt += int(temp)
print(rlt)