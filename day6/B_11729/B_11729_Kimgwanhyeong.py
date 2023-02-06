# 하노이의 탑 w 재귀함수
# idea : n 개의 원반을 옮긴다? n-1 개의 원반을 중간 기둥에 옮기고 n 번째 원반을 최종 기둥에 옮긴 후
# n-1 개의 원반을 최종 기둥에 옮긴다.

n = int(input())

def hanoi(n, first, second, last):  # 첫번째 기둥에서 n 개의 원반을 최종 기둥으로 옮기는 함수 정의
    # 원반이 한개라면 first에서 last로 한개 옮기고 끝
    if n == 1:
        print(first, last)
        return 
    
    # 원반이 한개가 아니라면 n-1 개를 중간 기둥으로 모두 옮기는 과정 수행(hanoi 함수로 첫번째에서 중간 기둥으로 이동)
    hanoi(n-1, first, last, second)

    # n 번째 원반을 첫번째에서 최종 기둥으로 옮김
    print(first, last)

    # 중간 기둥에 있는 n-1개를 최종 기둥으로 옮김
    hanoi(n-1, second, first, last)

# 옮긴 횟수를 출력
print(2**n - 1)
# 옮긴 과정을 출력
hanoi(n,1,2,3)