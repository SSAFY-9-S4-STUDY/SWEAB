import sys
sys.stdin = open("input.txt")

# 인풋값 N = 도시갯수, road = 거리길이, oil_price = 도시별 기름가격
N = int(input())
road = list(map(int, input().split()))
oil_price = list(map(int, input().split()))

# 변수설정
# 초기 기름값을 첫번째도시의 가격으로 설정
# 이동거리를 담아줄 meter변수, 답을 담아줄 ans 변수
oil = oil_price[0]
meter = 0
ans = 0

#  i는 1부터 N까지 <- i=0 일땐 위에 초기변수에서 설정했음
for i in range(1, N):
    # 미터에 이동거리 계속 더해줌
    meter += road[i-1]
    # 지금 기름 가격보다 더 싼 기름을 만나면 여태 온 거리*기름값 정답에 더해주고
    # 기름가격 갱신, 거리 초기화
    if oil_price[i] <= oil:
        ans += meter * oil
        oil = oil_price[i]
        meter = 0
# 더 싼 걸 못만나서 갱신 안된 기름가격과 거리만큼 마지막에 더해줌
ans += meter * oil 
  
print(ans)