def check(answer):
    for x, y, a in answer:
        if a == 0: # 기둥 체크
            if y == 0 or [x-1, y, 1] in answer or [x,y,1] in answer or [x,y-1,0] in answer:
                continue
            return False
        elif a == 1: # 보 체크
            if [x,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer) or [x+1,y-1,0] in answer:
                continue
            return False
    return True


# 첫 풀이 아이디어: 2차원 배열에 기둥과 보의 상태를 나타내주려했으나,
# 생각보다 기둥, 보의 조합이 너무 많아서 실패...
# 구글링한 결과 [x, y, a] 배열을 answer 배열에 넣고 빼면서
# answer 리스트 전체 탐색을 통해 가능 여부를 검증하는 방식
def solution(n, build_frame):
    answer = []
    for x, y, a, b in build_frame:
        if b == 1: # 설치
            # 일단 설치해놓고
            answer.append([x,y,a])
            # answer 리스트를 검증했을 때 불가능이면 설치 삭제
            if not check(answer):
                answer.remove([x, y, a])
            
        elif b == 0: # 삭제
            answer.remove([x,y,a])
            if not check(answer):
                answer.append([x,y,a])
    
    answer.sort()

    return answer