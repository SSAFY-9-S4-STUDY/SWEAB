from itertools import permutations


def solution(n, weak, dist):
    length = len(weak)
    # 일자로 만들기
    weak.extend([w + n for w in weak])

    # 친구를 투입할 때마다 필요한 최소 친구 수
    answer = len(dist) + 1

    # 각 취약 지점마다 시작점으로 설정
    for start in range(length):
        for friends in permutations(dist):
            count = 1  # 투입되는 친구 수
            position = weak[start] + friends[count - 1]  # 현재 친구가 점검할 수 있는 최대 위치

            # 시작점부터 마지막 취약 지점까지 확인
            for index in range(start, start + length):
                # 점검할 수 있는 위치를 벗어난 경우
                if position < weak[index]:
                    count += 1  # 새로운 친구를 투입
                    if count > len(dist):  # 더 이상 투입할 친구가 없다면 끝
                        break
                    position = weak[index] + friends[count - 1]

            answer = min(answer, count)  # 최소 친구 수 업데이트

    if answer > len(dist):
        return -1

    return answer


print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))  # return 2


# 원형이니까 외벽 일자로 만들어서 풀기
# 일부 테스트 케이스에서 오답

# def solution(n, weak, dist):
#     weak_length = len(weak)
#     # 일자로 만들기
#     weak.extend([w + n for w in weak])
#
#     dist.sort(reverse=True)  # 먼 순서대로 정렬
#     answer = len(dist) + 1  # 친구를 최대로 사용하는 경우로 초기화
#
#     # 모든 취약 지점을 시작점으로 설정
#     for start in range(weak_length):
#         friend_idx = 0  # 사용할 친구의 인덱스
#         count = 0  # 사용된 친구의 수
#         position = weak[start] + dist[friend_idx]  # 커버할 수 있는 마지막 위치
#
#         for i in range(start, start + weak_length):  # 커버해야 할 취약 지점을 순회
#             if position < weak[i]:  # 커버할 수 있는 범위를 벗어나면
#                 count += 1  # 친구 추가
#                 friend_idx += 1  # 다음 친구로 넘어감
#                 if friend_idx == len(dist):  # 투입할 수 있는 친구가 더 이상 없으면 종료
#                     break
#                 position = weak[i] + dist[friend_idx]  # 커버할 수 있는 새로운 마지막 위치
#
#         answer = min(answer, count + 1)  # 투입된 친구의 수를 업데이트
#
#     if answer > len(dist):  # 모든 친구를 투입해도 취약 지점을 커버할 수 없는 경우
#         return -1
#
#     return answer
#
#
# print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))


# 이것도 못 풀엇음ㅎ
# import java.util.Arrays;
#
# public class Solution {
#     public int solution(int n, int[] weak, int[] dist) {
#         int weakLength = weak.length;
#         int[] extendedWeak = new int[weakLength * 2];
#
#         for (int i = 0; i < weakLength; i++) {
#             extendedWeak[i] = weak[i];
#             extendedWeak[i + weakLength] = weak[i] + n;
#         }
#
#         Arrays.sort(dist);
#         int answer = dist.length + 1;
#
#         for (int start = 0; start < weakLength; start++) {
#             int friendIdx = dist.length - 1; // 가장 멀리 갈 수 있는 친구부터 시작
#             int count = 0;
#             int position;
#
#             for (int i = start; i < start + weakLength; friendIdx--) { // weakLength 만큼 확인
#                 if (friendIdx < 0) { // 친구를 더 이상 투입할 수 없으면 끝
#                     break;
#                 }
#
#                 position = extendedWeak[i] + dist[friendIdx];
#                 count++;
#
#                 while (i < start + weakLength && position >= extendedWeak[i]) { // 다음 취약지점 체크
#                     i++;
#                 }
#             }
#
#             answer = Math.min(answer, count);
#         }
#
#         if (answer > dist.length) {
#             return -1;
#         }
#
#         return answer;
#     }
#      // 테스트 케이스
#     public static void main(String[] args) {
#         Solution sol = new Solution();
#         System.out.println(sol.solution(12, new int[]{1, 5, 6, 10}, new int[]{1, 2, 3, 4}));
#     }
# }

