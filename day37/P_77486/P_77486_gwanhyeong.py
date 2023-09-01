def solution(enroll, referral, seller, amount):
    
    def divide(person, money):
        nonlocal answer
        if (money == 0) or (person == "-"):
            return
        index = seq_dict[person]
        answer[index] += money - money // 10
        recommender = referral[index]
        return divide(recommender, money // 10)

    n = len(enroll)
    answer = [0 for _ in range(n)]
    seq_dict = dict()
    # for i in range(n):
    #     seq_dict[enroll[i]] = i
    for i, name in enumerate(enroll):
        seq_dict[name] = i

    # for i in range(len(seller)):
    #     person = seller[i]
    for i, person in enumerate(seller):
        money = amount[i] * 100
        divide(person, money)

    return answer