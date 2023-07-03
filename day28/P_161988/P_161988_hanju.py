def solution(sequence):
    # ans: 정답을 담을 변수
    # plus, minus = 연속 펄스를 적용한 리스트에서의 부분합을 저장할 변수
    ans, plus, minus = abs(sequence[0]), -1, -1
    for i in range(len(sequence)):
        # 현재 인덱스에서 연속 펄스를 적용한 숫자들
        tmp_plus, tmp_minus = sequence[i] * (-1)**i, sequence[i] * (-1)**(i+1)
        # 이전값과 비교하여 이전값과 연속할지 말지 선택
        # 즉, 이 값들은 현재 인덱스가 가장 오른쪽에 있을 때 최대가 되는 부분합
        plus = plus + tmp_plus if plus > 0 else tmp_plus
        minus = minus + tmp_minus if minus > 0 else tmp_minus
        # 구한 현재 인덱스의 값을 통해 최대값 갱신
        ans = max(ans, plus, minus)

    return ans

print(solution([2, 3, -6, 1, 3, -1, 2, 4]))