T = int(input())
for tc in range(1, T+1):
    N, K = map(int,input().split())
    students = list(map(int,input().split()))
    
    total_stu = list(range(N+1))
    for i in students:
        total_stu.remove(i)
    print(f'#{tc}', *total_stu[1:])