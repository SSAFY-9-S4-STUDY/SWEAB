import sys
sys.stdin = open('input.txt', 'r')

# 구글링 했습니다 ㅎㅎㅎ
# 변수명만 취향에 맞게 바꿨어요
def quick_sort(L, R):
    if R <= L:
        return

    M = partition(L, R)
    quick_sort(L, M - 1)
    quick_sort(M, R)

def partition(L, R):
    pivot = nums[(L + R) // 2]
    while L <= R:
        while nums[L] < pivot:
            L += 1
        while nums[R] > pivot:
            R -= 1
        if L <= R:
            nums[L], nums[R] = nums[R], nums[L]
            L, R = L + 1, R - 1
    return L


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    quick_sort(0, N-1)

    print(f'#{test_case} {nums[N//2]}')
