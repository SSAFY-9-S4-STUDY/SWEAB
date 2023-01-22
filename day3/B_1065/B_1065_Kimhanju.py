def solution(n):
    if int(n) < 100:
        return int(n)
    else:
        lst_nums = list(map(int,list(str(n))))
        lst_sub = [lst_nums[i+1] - lst_nums[i] for i in range(len(lst_nums)-1)]
        return solution(n-1)+1 if len(set(lst_sub)) == 1 else solution(n-1)

N = int(input())

print(solution(N))