# hanoi_dict = {1 : [], 2 : [], 3 : []}

# count = 0

# def hanoi(n):
#     if n == 1:
#         hanoi_dict[3].append(1)


# hanoi(int(input()))

# print(hanoi_dict)

'''
이 문제를 풀기 위해서 재귀함수에 대해서 공부를 하기는 했는데...
머릿속으로 잡힐 듯 말 듯 하면서도... 3번째 원판부터 다른 기둥으로 옮길 때
이미 있으면 재귀함수를 또 써야 하나... 하 뭐지 이런 생각으로 몇 시간 보내니
그냥 여러 사람의 답을 보고 공부하고 시간이 지나서 혼자 써보는 게 좋을 거 같다는
생각이 들어서 아래에는 제가 보고 공부한 코드를 달아두도록 하겠습니다 ㅠ
재귀는 아직 익숙하지가 않아서 여러 예제를 풀어봐야할 거 같아요...

배운점
1. 재귀함수를 잘 활요앟려면 함수의 '추상화'성질을 잘 생각할 필요있음
2. 입력값이 하나라고 함수 설정에서 parameter를 하나로 둘 필요없음.
'''
# case 1
# 출처(real_jun9u.log)
# https://velog.io/@real_jun9u/%EB%B0%B1%EC%A4%80%ED%8C%8C%EC%9D%B4%EC%8D%AC-11729%EB%B2%88-%ED%95%98%EB%85%B8%EC%9D%B4-%ED%83%91-%EC%9D%B4%EB%8F%99-%EC%88%9C%EC%84%9C
n = int(input())
def hanoi(n,a,b,c):
    if n == 1:
        print(a,c)
    else:
        hanoi(n-1,a,c,b)
        print(a,c)
        hanoi(n-1,b,a,c)
count = 0
for _ in range(n):
    count = 2*count + 1
print(count)
hanoi(n,1,2,3)

# case 2
# 출처(초보몽키의 개발공부로그)
# https://wayhome25.github.io/cs/2017/04/15/cs-16-1-recursion/
def hanoi(num, _from, _by, _to):
    # 탈출 조건
    if num == 1:
        print('{}에서 {}로 {}번째 원반 이동'.format(_from, _to, num))
        return
    hanoi(num-1, _from, _to, _by)
    print('{}dptj {}로 {} 번째 원반 이동'.format(_from, _to, num))
    hanoi(num - 1, _by, _from, _to)

while 1:
    numOfTray = int("원반의 개수를 입력하세요!(종료 : 0)")

    if numOfTray == 0:
        break
    hanoi(numOfTray, 'A', 'B', 'C')