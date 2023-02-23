"""
n = int(input())

meeting = dict()

temp = []

for i in range(n):
    temp_start, temp_end = map(int, input().split())
    temp.append((temp_start, temp_end))
    if meeting.get(temp_start) == None:
        meeting[temp_start] = [temp_end]
    else:
        meeting[temp_start].append(temp_end)

meeting = dict(sorted(meeting.items(), key= lambda x: (x[0], x[1])))

starting_point = list(meeting.keys())[0]
end_point = max(meeting.keys())

queue = []
best = 0

for time in meeting.keys():  
    if meeting.get(starting_point)[0] <= time:
        break
    queue.append(([time], 0))
    while queue:  # 피해야하는 시간들 어카지.. bfs 쓰면 검사 다 할 수 있긴 하다..
        now = queue.pop(0)
        if best < now[1]:
            best = now[1]
        for candidate in now[0]:
            if meeting.get(candidate):
                queue.append((meeting.get(candidate), now[1] + 1))
            else:
                while candidate <= end_point:
                    candidate += 1
                    if meeting.get(candidate):
                        queue.append((meeting.get(candidate), now[1] + 1))
                        break
    
print(best)
"""
# 새 풀이
n = int(input())

quest = []
for _ in range(n):
    quest.append(tuple(map(int, input().split())))

quest = sorted(quest, key= lambda x: (x[1], x[0]))

count = 1
end_point = quest[0][1]
for i in range(1, n):
    if quest[i][0] >= end_point:
        count += 1
        end_point = quest[i][1]

print(count)
    