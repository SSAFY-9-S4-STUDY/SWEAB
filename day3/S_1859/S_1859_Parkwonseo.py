T = int(input())
for x in range(1, T + 1):
    N = int(input())
    trade_cost = list(map(int, input().split()))
    total_benefit = 0
    # len[:trade_cost.index(max(trade_cost))] * max(trade_cost) - sum(trade_cost[0:trade_cost.index(max(trade_cost))])
    # max_index = max(trade_cost[trade_cost.index(max(trade_cost)) + 1:])
    # max_index가 계속 갱신되어야 한다.
    max_index = 0
    min_index = 0
    for i in range(N):
        if i == min_index:
            max_index = trade_cost[i:].index(max(trade_cost[i:])) + i
            # 슬라이싱 하면 index를 슬라이싱 시작부터 잡는다.

        if i == max_index:
            total_benefit += ((max_index - min_index) * trade_cost[max_index]) - sum(trade_cost[min_index:max_index])
            min_index = i + 1

    print(f'#{x} {total_benefit}')