"""
조건
n : 외벽의 총 둘레
weak : 취약 지점의 위치, 오름차순
dist : 각 친구가 1시간동안 이동가능한 거리

결과값
return '취약지점을 모두 점검하기 위해 보내야 하는 친구 수의 최솟값' 구하기

꿀팁 (모르겠어서 구글링 했습니다..)
- 원형으로 구성되어 있을 때는 길이를 2배로 해서 원형 -> 일자 로 작업하는것이 편하다! 
"""

from itertools import permutations


def solution(n, weak, dist):
    # weak배열의 길이
    len_weak = len(weak)
    # weak배열의 길이를 2배로 늘리기
    weak = weak + [weak[i] + n for i in range(len_weak)]

    # 투입할 친구수의 최솟값을 찾기 위해 미리 친구수의 최댓값 + 1로 초기화
    answer = len(dist) + 1

    # 취약지점에서 출발
    for start in range(len_weak):
        # 경우의 수 각각에 대해
        for friends in list(permutations(dist, len(dist))):
            # 점검 인원 1명으로 시작
            count = 1
            # 도착지점 = 출발지점 + 친구가 가능한 최대 거리
            position = weak[start] + friends[count - 1]
            # 출발 지점에서부터 하나씩 모든 지점을 살펴보며
            for i in range(start, start + len_weak):
                # 최대 가능 거리를 갔음에도 여전히 점검할 지점이 남아있는 경우
                if position < weak[i]:
                    # 친구를 한명 더 투입
                    count += 1
                    # 더이상 투입할 친구가 없는 경우, break
                    if count > len(dist):
                        break
                    # 새로운 친구의 도착 지점 갱신
                    position = weak[i] + friends[count - 1]
            # 경우의 수를 살펴보면서, 더 적은 인원으로 갱신
            answer = min(count, answer)
    # 필요한 친구 수가 주어진 친구 수보다 많을 경우, -1 반환
    if answer > len(dist):
        return -1
    return answer
