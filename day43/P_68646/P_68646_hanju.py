def solution(a):
  # 1. 변수 설정
  # a의 길이
  N = len(a)
  # 0: 자신이 젤 작음, 1: 왼쪽 혹은 오른쪽 한 군데에 자기보다 작은 수 존재, 2: 왼쪽 오른쪽 둘 다 존재
  cnt_arr = [0] * N

  # 2. 최솟값 이중배열 갱신
  min_left = a[0]  # 왼쪽 풍선 중 최솟값(초기값 0번 인덱스)
  min_right = a[-1]  # 오른쪽 풍선 중 최솟값(초기값 -1번 인덱스)
  for i in range(1, N):
    # 왼쪽에 자기 자신보다 작은 수가 존재하는지 판단
    if min_left < a[i]: cnt_arr[i] += 1
    else: min_left = a[i]  # 아니면 왼쪽 최솟값 갱신
    # 오른쪽에 자기 자신보다 작은 수가 존재하는지 판단
    if min_right < a[-i-1]: cnt_arr[-i-1] += 1
    else: min_right = a[-i-1] # 아니면 오른쪽 최솟값 갱신

  # 3. 연산이 끝난 cnt_arr를 순회하며 정답 도출
  answer = 0
  for cnt in cnt_arr:
    if cnt != 2: answer += 1
  return answer

print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))