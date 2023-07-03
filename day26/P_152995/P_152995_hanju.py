def solution(scores):
    # 완호의 점수
    my_a, my_b = scores[0]
    my_sum = my_a + my_b
    # 성적을 석차별로 정렬
    ordered_scores = sorted(scores, key=lambda x:(-x[0], x[1]))
    # 정렬한 배열을 순회하며 완호의 석차 구하기
    ans, max_b = 1, 0
    for a, b in ordered_scores:
        # 최고점 갱신
        max_b = max(max_b, b)
        # 인센티브를 못 받는 경우
        if my_a < a and my_b < b:
            return -1
        # 석차가 뒤로 밀려남
        if my_sum < a + b and b >= max_b:
            ans += 1
    return ans

print(solution([[2,2],[1,4],[3,2],[3,2],[2,1]]))