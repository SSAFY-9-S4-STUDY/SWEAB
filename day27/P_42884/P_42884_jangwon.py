def solution(routes):
    answer = 0
    # 여기서부터 문제 해결
    # 경계점을 기준으로 판단하는 것이 카메라를 가장 적게 설치하게 됨.
    # 종료지점을 기준으로 정렬을 하자.
    routes.sort(key=lambda x: x[1])

    # 제일 첫 종료지점에 카메라 설치하고 다음 범위 내에 있는지 판단하고
    # 없다면 다음 종료지점을 카메라로 새롭게 할당.
    camera = routes[0][1]
    count = 1

    for arr in routes[1:]:
        if arr[0] <= camera <= arr[1]:  # 범위 안에 있다면
            continue
        else:  # 범위 안에 없다면,
            camera = arr[1]
            count += 1
            
    answer = count
    return answer

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))