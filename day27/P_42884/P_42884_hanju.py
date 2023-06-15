def solution(routes):
    end_point, ans = -30001, 0
    sorted_routes = sorted(list(map(lambda x: [max(x), min(x)], routes)))
    for e, s in sorted_routes:
        if s > end_point:
            end_point = e
            ans += 1
    return ans

routes = [[-20,-1], [-19,-10], [-9,1]]
print(solution(routes))