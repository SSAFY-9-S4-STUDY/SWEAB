import sys
sys.stdin = open("input.txt")

arr = input()

arr_cal = ''  # 나중에 계산해줄 식
num = ''  # 숫자를 담아 나중에 int로 변환 str가 001이 되는 반례 소거
cnt_a = 0  # '(' 의 갯수
cnt_b = 0  # ')' 의 갯수


for i in range(0, len(arr)-1):
    if arr[i] == '-':
        arr_cal += arr[i] + '('
        cnt_a += 1
    elif arr[i] == '+':
        arr_cal += arr[i]
    else:
        num += arr[i]
        if arr[i+1] == '+':
            arr_cal += str(int(num))
            num = ''
        if arr[i+1] == '-':
            if cnt_a >= 1:
                arr_cal += str(int(num)) + ')'
                cnt_b += 1
        # 첫 등장하는 '-' 앞에 닫는 괄호 생기는 반례 소거
            else :
                arr_cal += str(int(num))
            num = ''

# 맨 마지막은 무조건 숫자
num += arr[-1]
arr_cal += str(int(num))    
    
if cnt_a != cnt_b:  # 닫는 괄호가 하나 적은 경우 마지막에 닫아줌
    arr_cal += ')'

print(eval(arr_cal))