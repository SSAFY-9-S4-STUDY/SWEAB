# 이용한 성질
# A, B, C 세 수가 M 으로 나눈 나머지가 같다면
# A = M*a +r
# B = M*b +r
# C = M*c +r
# (B-A) =M *(b-a)
# (C-A) =M *(c-a) 
# 따라서 인풋으로 받은 모든 수의 min 값을 빼주고 공배수 구하면 됨. 


N = int(input())
numbers = [int(input()) for _ in range(N)]
first = min(numbers)
numbers = [i - first for i in numbers if i - first != 0]

new_min = min(numbers) 
temp_list = []
for i in range(2,new_min+1):
    for a in numbers:
        if a % i:
            break
    else:
        temp_list.append(i)

print(*sorted(temp_list))

