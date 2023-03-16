# Day11 Code Review

## 김한주 > 김주연

- B 11725 : 코드 깔끔하네요. 시작 정점인 1 방문 처리해서 중복 연산 막아주시면 더 좋을 거 같아요!  
`par = [1000] + [0 for _ in range(N)]` 여기서 [1000]을 맨 앞에 넣어주는 이유도 궁금합니다
- B 18258 : 전 바로바로 결과를 출력했었는데 리스트에 결과값을 한데 모아 출력하는 방식 참신하네요.
- B 24444 : 순회 순서를 출력하는 문제라 처음 풀 때 엄청 해맸던 기억이 납니다. 전 이 문제 deque 안 쓰면 시간 초과 뜨던데 신기하네요...
- B 24479 : dfs 깔끔하게 구현해주셔서 이해하기 편했습니다 ㅎㅎ

## 김관형 > 류동훈

- B 11725 : 스택을 이용해서 DFS 을 이용했군요! top의 의미를 살려서 `top = -1 / top += 1` 쓴 코드가 인상적입니다.
- B 18258 : 명령 개수가 2,000,000 이하라서 빈 큐 길이가 2000000이군요! 전 빈 리스트에 append했더니 시간초과 떴던거 같은데 아예 `[0]*N` 이런 식으로 만들어 놓으면 훨씬 빠르겠네요
- B 24444 : 깔끔합니다! 여기도 `rear=-1` 이후에 `rear+=1` 보이네요ㅎㅎ
- B 24479 : DFS 깔끔한 코드! bb

## 이장원 > 박원서

- B 11725 : 나는 dfs로 풀었는데, bfs로 푸는 방법은 이렇게 할 수 있구나라는 걸 확인할 수 있었어! 담에는 나도bfs로 풀어볼게!!
- B 18258 : 나도 비슷하게 풀이를 해서 반갑고 깔끔합니당 bb
- B 24444 : 이 코드도 나랑 비슷하고 깔끔합니당 역쉬~!! cf. 나는 deque 안써서 처음에는 시간초과나왔었어 ㅜ
- B 24479 : 나는 재귀로 풀어서 계속 시간 초과나왔는데, 형 방법처럼 stack으로 풀어나가면 괜찮다는 걸 알았어! 너무 재귀에 의존하면 피볼 수 있음을 안 거 같어...!

## 김주연 > 임준수

- B 11725 : 깔끔해서 따로 피드백 드릴 점은 없습니다. 런타임 에러 떠서 deque 라이브러리 사용하신 거겟죠?!
- B 18258 : 문제 특성상 퓨는 방법은 거의 모두 동일할 듯 합니당 ㅎㅎ 다만 저는 시간 넘 오래걸려서 바로바로 print 안해주고 리스트안에 모아서 한번에 프린트했어요!! 두 방법 모두 숙지하면 나중에 필요할 일이 있을수도 잇을 거 같아
- B 24444 :  bfs 정석 풀이네요 피드백 엄슴 고생하셨습니다!
- B 24479 : dfs 정석 풀이네요 피드백 엄슴 고생하셨습니다!

## 류동훈 > 서재현

- B 11725 : 저는 DFS로 풀었는데 BFS로 푸신 점이 인상깊었습니다! 개인적으로 deque사용법도 알 수 있어서 많은 것을 배울 수 있는 코드였습니다. 마지막에 visited[2::] 이거는 visited[2:]랑 같지 않나요? :가 2개 들어가면 의미가 달라지는지 궁금합니다!
- B 18258 : deque 사용법이 front rear보다 훨씬 간편하네요!
- B 24444 : 순서에 1을 더함과 동시에 visited에 적용하면서 겹치는 부분을 사전에 차단한 점이 깔끔하고 좋았습니다. 저는 항상 bfs할 때 visited 2번씩 사용했었는데 앞으로 저도 이 방법 사용할 것 같네요. 감사합니답!
- B 24479 : deque 활용해서 dfs구현했으면 더 좋았을 것 같은 개인적인 느낌...? 다른 문제들이 모두 deque를 활용하셔서 dfs는 어떻게 활용하시나 기대했습니다 ㅎㅎㅠ 하지만 재귀도 너무 깔끔하고 좋았습니다!!


## 박원서 > 김한주

- B 11725 :
- B 18258 :
- B 24444 :
- B 24479 :

## 임준수 > 김관형

- B 11725 : 비슷하게 풀어주셨습니다. 함수로 따로 만들어 줘서 보기 편한 것 같습니다!
- B 18258 : 문제에서 풀이방법을 명확하게 제시해줘서 풀이가 같습니다! 고생하셨습니다
- B 24444 : 역시나 풀이가 같습니다! 깔끔한 BFS 풀이입니다
- B 24479 : 역시 깔끔한 풀이입니다! 재귀함수 이용해서 풀어보시는 것도 추천해드립니다

## 서재현 > 이장원

- B 11725 :  
` N = int(sys.stdin.readline().rstrip())`  
`n1, n2 = map(int, sys.stdin.readline().rstrip().split())`  
이 부분에서 혹시 `readline()`까지만 구현했을 때 뒤에 '\n'이 붙어서 `rstrip()` 해준거면 굳이 안해줘도 돼!  
왜냐하면 int()나 map()을 통해서 문자열을 int형으로 변환시켜줄때 자동으로 '\n'는 삭제가 되거든. 이외 나머지는 깔끔.
- B 18258 :   
나도 이번 문제 풀면서 `deque()` 사용했는데, 얻는 장점이 많더라구. 내가 알아본 몇 가지 장점만 소개해줄게.     
    1. 엄격한 리스트를 만들 수 있다.
    2. 속도가 리스트에 비해 굉장히 빠르다. List = O(n), deque = O(1)
    3. 당연하지만 큐작업이 훨씬 편해진다.
- B 24444 :   
나랑 코드 로직이 대체로 비슷해서 이해하기 수월했고 굉장히 깔끔한 느낌을 받았어.  
교수님이 말씀해주신 거에 근거해서 진짜진짜 별거 아니지만 하나만 꼬집자면..  
`def dfs(start)` 같이 함수 정의하는 부분은 이제 메인 코드 바깥으로 꺼내서 적으라고 하시드라구.  
여기 코드에서는 N, M, R 변수 입력 받는 라인 위로 올려주면 될 거 같아!
- B 24479 :   
코멘트 없습니다. 깔끔한 평양냉면 코드네요. 장원씨 수고 많았어요ㅜㅜ
