

def quick_sort(A, l, r):
    if l < r:
        p = partition(A, l, r)
        quick_sort(A, l, p - 1)
        quick_sort(A, p + 1, r)

def partition(A, l, r):
    pivot = (l + r) // 2
    while l < r :
        while(A[l] < A[pivot] and l < r):
            l += 1
        while(A[r] >= A[pivot] and l < r):
            r -= 1
        if l < r:
            if l == pivot:
                pivot = r
            A[l], A[r] = A[r], A[l]
    A[pivot], A[r] = A[r], A[pivot]
    return r

for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    quick_sort(a, 0, n-1)
    print(f"#{t+1} {a[n//2]}")