from math import gcd

N = int(input())

num_lst = [int(input()) for _ in range(N)]
num_lst.sort()
# 입력받은 숫자들을 정렬하여 인접한 순서 간 숫자를 뺀 결과를 저장할 리스트를 변수에 할당
new_lst = []
for i in range(1, N):
    new_lst.append(num_lst[i]-num_lst[i-1])

# 숫자를 뺀 결과들의 최대공약수를 구한다.
prev = new_lst[0]
for i in range(1,len(new_lst)):
    prev = gcd(prev, new_lst[i])
# prev = gcd(*new_lst)  # 위와 같은 결과


# 최대 공약수의 약수 중 1을 뺀 나머지를 divisor_lst에 넣어준다.
divisor_lst = []
for num in range(2,int(prev**(1/2))+1):
    if prev % num == 0:
        divisor_lst.append(num)
        divisor_lst.append(prev // num)
divisor_lst.append(prev)
# 중복된 값이 있는 경우를 대비한 코드
divisor_lst=list(set(divisor_lst))
# 오름차순으로 출력하기 위해
divisor_lst.sort()

print(*divisor_lst)