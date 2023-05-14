import math

def binarytree(binary, parent):
    if len(binary) == 1:
        if parent == '0' and binary == '1':
            return 0
        return 1

    mid = len(binary)//2
    
    left = binary[:mid]
    right = binary[mid+1:]

    next_mid_idx = len(left) // 2

    if parent == '0' and (left[next_mid_idx]=='1' or right[next_mid_idx]=='1'):
        return 0
    
    if not binarytree(left, left[next_mid_idx]) or not binarytree(right, right[next_mid_idx]):
        return 0
    
    return 1


def solution(numbers):
    answer = []
    
    for number in numbers:
        # 이진수 변환 후 자릿수 맞춰주기
        binary_number = bin(number)[2:]
        digit = 2 ** (int(math.log(len(binary_number), 2)) + 1) - 1
        binary_number = '0' * (digit - len(binary_number)) + binary_number
        # print(binary_number)

        if binary_number[digit//2] == '0':
            result = 0
        else:
            result = binarytree(binary_number, 1)
        answer.append(result)
        
    return answer

