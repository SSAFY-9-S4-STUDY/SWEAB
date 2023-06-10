def solution(play_time, adv_time, logs):
    if play_time == adv_time:
        return "00:00:00"
    
    play_time = time_to_sec(play_time)
    adv_time = time_to_sec(adv_time)
    dp = [0 for _ in range(play_time + 1)]
    
    for log in logs:
        start = time_to_sec(log[:8])
        end = time_to_sec(log[9:])
        dp[start] += 1
        dp[end] -= 1
        
    for i in range(1, len(dp)):
        dp[i] = dp[i] + dp[i-1]
        
    for i in range(1, len(dp)):
        dp[i] = dp[i] + dp[i-1]
    
    most = 0
    ans_time = 0
    
    for i in range(adv_time - 1, play_time):
        if i >= adv_time:
            if most < dp[i] - dp[i - adv_time]:
                most = dp[i] - dp[i - adv_time]
                ans_time = i - adv_time + 1
        else:
            if most < dp[i]:
                most = dp[i]
                ans_time = i - adv_time + 1
    return sec_to_time(ans_time)

def time_to_sec(time):
    h = int(time.split(':')[0]) * 3600
    m = int(time.split(':')[1]) * 60
    s = int(time.split(':')[2])
    
    return h + m + s

def sec_to_time(sec):
    h = sec // (60 * 60)
    sec %= (60 * 60)
    m = sec // 60
    sec %= 60
    s = sec
    
    return '%02d:%02d:%02d' % (h, m, s)