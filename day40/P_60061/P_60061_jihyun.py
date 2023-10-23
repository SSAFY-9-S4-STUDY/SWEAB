def check(answer, x_stand, y_stand):
    for x, y, a in answer:
        if x < x_stand -1 or x_stand + 1 < x or y < y_stand -1 or y_stand + 1 < y:
            continue
        if a == 0:
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            return False
        elif a == 1:
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []
    
    for x, y, a, b in build_frame:
        # 설치일 경우, 일단 추가 후 확인
        if b == 1:
            answer.append([x, y, a])
            if not check(answer, x, y):
                answer.remove([x, y, a])
        else:
            answer.remove([x, y, a])
            if not check(answer, x, y):
                answer.append([x, y, a])
    # print('정렬 전', answer)
    result = [[1, 0, 0], [1, 1, 1], [2, 1, 0], [2, 2, 1], [5, 1, 1], [5, 1, 0], [4, 2, 1], [3, 2, 1]]
    result.sort()
    print(result)
    
    answer.sort()
    return answer