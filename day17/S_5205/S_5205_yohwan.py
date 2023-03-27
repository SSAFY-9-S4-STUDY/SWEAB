import sys
sys.stdin = open("input.txt")

# 퀵정렬 시작
def quick_sort(start, end):
    # 배열이 1일 경우 리턴
    if start >= end :
        return
    
    # 분할할 리스트의 첫 요소를 pivot으로 설정
    pivot = start
    left = start+1
    right = end-1

    # 좌우에서 pivot과 비교
    # left가 pivot보다 작으면 +1 이동 right가 pivot보다 크면 -1이동
    # 좌측엔 pivot보다 작고 우측엔 pivot보다 큰숫자만 놓기 위해
    while left <= right:
        while left <= right and arr[left] <= arr[pivot]:
            left += 1
        while left <= right and arr[right] >= arr[pivot]:
            right -= 1
        # 좌측에서 pivot보다 큰 값, 우측에서 작은 값이 나타나면 좌우 자리바꾸기
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]

    # 반복문 다 끝나고 pivot이 정렬된 수열에서의 자기의 위치에 놓임
    # 그리고 재귀
    arr[pivot], arr[right] = arr[right], arr[pivot]
    quick_sort(start, right)
    quick_sort(right+1, end)


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    
    quick_sort(0, len(arr))
    ans = arr[N//2]
    
    print(f'#{test_case} {ans}')