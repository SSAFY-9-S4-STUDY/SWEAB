# t = int(input())
# for test_case in range(1,t+1):
#     floor, many, num = map(int,input().split())
#     hosu = (num // floor) + 1
#     cheong = num % floor
#     if hosu < 10:
#         print(str(cheong)+'0'+str(hosu))
#     else:
#         print(str(cheong)+str(hosu))

# # 틀렸습니다... 그럼 반례가 뭐야??
# # 이 경우 cheong이 num 을 floor 로 나눈 나머지라고 했는데, 나머지는 0 <= cheong<floor.
# # 하지만 내가 만들고 싶은건 0일때, 즉 floor의 배수인 경우 0이 아니라 floor가 나와야함
# for _ in range(t):
#     floor, w, num = map(int, input().split())
#     hosu = (num // floor) + 1
#     cheong = num % floor
#     if cheong:
#         if hosu < 10:
#             print(str(cheong)+'0'+str(hosu))
#         else:
#             print(str(cheong)+str(hosu))
#     else:
#         if hosu < 10:
#             print(str(floor)+'0'+str(hosu))
#         else:
#             print(str(floor)+str(hosu))
#### 위는 틀렸습니다.
t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())
    num = n//h + 1
    floor = n % h
    if n % h == 0:
        num = n//h
        floor = h
    print(f'{floor*100+num}')


