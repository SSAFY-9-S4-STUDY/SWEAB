def solution(enroll, referral, seller, amount):
    answer = [0] * (len(enroll))
    # index함수는 시간복잡도가 구리다. dict가 좋다 라고함
    # 딕셔너리를 만드는데 enroll : 번호 구조가 되게 만듬
    mem_dict = dict(zip(enroll,range(len(enroll))))
    
    for i in range(len(seller)):
        # seller가 누군지 파악 하기 위한 who 변수
        who = seller[i]
        price = 100 * amount[i]
        # who가 "-" 즉, 부모가 없다면 while문 종료.
        # 판매가를 10으로 나누지 못할때도 종료
        while who != "-":
            # who의 번호를 파악해서 이를 referral에 넣어 who의 부모를 찾는데 사용
            index = mem_dict[who]
            pay = price // 10
            answer[index] += price - pay
            price = pay
            who = referral[index]
            if pay == 0 : break
    return answer