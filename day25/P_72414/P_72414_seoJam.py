# 시분초에서 초 단위로 바꾸는 함수
def time_to_sec(time):
    h, m, s = map(int, time.split(':'))
    return h * 3600 + m * 60 + s

# 초 단위에서 시분초로 바꾸는 함수
def sec_to_time(sec):
    h = sec // 3600
    m = (sec % 3600) // 60
    s = sec % 60
    return "{:02d}:{:02d}:{:02d}".format(h, m, s)


def solution(play_time, adv_time, logs):
    # [0] 영상시간과 광고시간이 일치할 때
    if play_time == adv_time:
        return "00:00:00"

    # [1] 초 단위로 통일
    play_time = time_to_sec(play_time)
    adv_time = time_to_sec(adv_time)

    # [2] dp에 log별 시간정보 저장(구간합)
    dp = [0 for _ in range(play_time+1)]
    for log in logs:
        log_s, log_e = map(time_to_sec, log.split('-'))
        dp[log_s] += 1
        dp[log_e] -= 1
    for i in range(1, play_time+1):  # 구간값 저장
        dp[i] += dp[i-1]
    for i in range(1, play_time+1):  # 누적합 저장
        dp[i] += dp[i-1]

    # [3] 광고 시작시간 구하기
    max_temp, answer = dp[adv_time], 0  #=> max_temp를 0에서 dp[adv_time]으로 바꾸니까 정답됨. 이유 모름..
    for start in range(1, play_time):
        end = min(play_time, start+adv_time)
        temp = dp[end] - dp[start]
        if max_temp < temp:
            max_temp = temp
            answer = start + 1

    return sec_to_time(answer)