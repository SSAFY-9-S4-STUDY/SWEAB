def solution(enroll, referral, seller, amount):
    # 1. 변수 선언
    # 조직원수, 판매건수
    num, sell = len(enroll), len(seller)
    # 조직원별 합산 금액
    enroll_dic = {e:0 for e in enroll}
    # 조직원별 참여시킨 사람
    parent = {enroll[i]:referral[i] for i in range(num)}

    # 2. 판매별 금액분배
    for s, a in zip(seller, amount):
        a = a * 100  # 판매금액
        # 판매금액을 위로 올라가면서 분배
        # 분배할 금액이 남아있거나 위 사람이 center가 아닐 때까지 지속
        while a and s != "-":
            # 위 사람에게 분배할 금액
            give = a // 10
            # 분배할 금액을 뺀 나머지를 자신의 보유 금액에 합산
            enroll_dic[s] += a - give
            # 분배받을 사람과 금액 갱신
            s, a = parent[s], give

    # 3. dictionary의 value를 리스트화
    return list(enroll_dic.values())


enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]
print(solution(enroll, referral, seller, amount))