def solution(n, weak, dist):
    # 1. 변수 설정

    # dist를 내림차순으로 정렬
    dist.sort(reverse=True)
    
    weak_dist = [n-weak[-1]+weak[0]]
    return weak_dist

print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))