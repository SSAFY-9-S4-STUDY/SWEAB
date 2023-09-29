"""
참고: https://glory-summer.tistory.com/229,
https://velog.io/@qweadzs/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%8B%A4%EB%8B%A8%EA%B3%84-%EC%B9%AB%EC%86%94-%ED%8C%90%EB%A7%A4Python,
https://kimmeh1.tistory.com/524,
gwanhyung's 풀이
"""
# 리프노드 -> 부모노드 -> 루트노드

def solution(enroll, referral, seller, amount):
    profits = [0 for _ in range(len(enroll))] # 각 판매원의 이익금
    dict = {}  # key, value = name, index
    for dict_index, dict_name in enumerate(enroll):
        dict[dict_name] = dict_index
    # print(dict)
    for s, a in zip(seller, amount):
        profit = a * 100  # 칫솔 당 100원
        while s != "-" and profit > 0: # 이익금 0원 이고 '-'만나면 종료
            index = dict[s]
            profits[index] += profit - profit//10 
            profit //= 10
            s = referral[index]
    return profits
