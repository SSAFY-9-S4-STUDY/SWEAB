# Day16 Code Review

## 김한주 > 김관형

- B 1260 : 재귀를 이용해서 깔끔하게 푸셨네요! 저는 반복문을 통해서 풀었는데 재귀가 훨씬 깔끔하네요
- B 12865 : 저랑 비슷하게 푸셨네요. 메모이제이션을 이용한 동적 계획법을 잘 이해하신 거 같습니다.
- B 20056 :

## 김관형 > 이장원

- B 1260 :
- B 12865 :
- B 20056 :

## 이장원 > 김주연

- B 1260 :
- B 12865 :
- B 20056 :

## 김주연 > 류동훈

- B 1260 :
- B 12865 :
- B 20056 :

## 류동훈 > 윤지현

- B 1260 : 캬 초기화 안하려고 1 -> 0 가는 거 기가 막힙니다. 저도 나중에 써먹겠습니다. 
- B 12865 : 저도 몰라유... 나는 겁나 고생해서 풀었는데 너무 간단하게 풀리고 이해도 안돼서 머리 아픔... 공부해야할 듯... ps 저도 처음에 dfs로 풀어서 써놨던 코드가 아까운 마음 천번만번 이해합니다만 밑에 코드는 읽진 않았습니다.
- B 20056 : 와우 좌표에 있는 파이어볼을 딕셔너리에 key는 튜플 value는 리스트로 만든거 진짜 좋습니다. 괜히 300ms가 아닌듯 리스트 내용도 진짜 깔끔하게 개수까지 적어놔서 나중에 연산까지 편하게 만들려는 설계 bbb

## 윤지현 > 문요환

- B 1260 : 가까운 곳부터 방문하려고 오름차순으로 `sort()` 해주는데 dfs 함수에서는 마지막 인덱스 값을 먼저 `pop()`하기 때문에 오름차순으로 sort해 놓은걸 다시 `reversed()`해서 작은 숫자가 뒤로가게 stack에 추가하시네요. 뭔가 더 효율적인 방법이 있을 것 같은데 제가 바쁘니 나중에 생각나면 공유해볼게요 ><
- B 12865 : 선배님 고생하셨군
- B 20056 : 순서대로 깔끔하게 푸셨네요

## 문요환 > 박원서

- B 1260 :
- B 12865 :
- B 20056 :

## 박원서 > 임준수

- B 1260 : 저는 다 담고 프린트하는 것만 생각했는데, 함수의 목적을 출력으로 생각하면 메모리를 많이 아낄 수 있군요..! 그러기 위해선 재귀로 풀어야하는데, 너무 좋은 것 같습니다. 제 개인적으로는 정석적인 풀이라고 생각이 드네요..!
- B 12865 : 크게 문제될 것은 없지만, 6~7번 줄을 queue.append(tuple(map(int, input().split())))으로 바꾸어 주면 변수할당을 다로 해줄 필요가 없을 것 같아요! 그 외에는 저와 코드가 거의 같아요!
- B 20056 : 13줄에서 변수를 각각 설정해주고 담으니 훨씬 이해가 편하네요.. 변수를 따로 담는 이점도 생각을 해볼 수 있어서 좋았습니다! 33~36에서 `state` 값이 `+= 1` 이거나 `= -1` 인것이, count와 abs(state)의 비교로 나뉘어진 파이어볼 방향을 설정해주는 부분에서 에러가 나왔을 수 있다는 생각이 드네요. 매번 노가다가 익숙해서 요소 하나만 바꿔주는것을 다 써버리는게 제 나쁜습관이라 생각했는데, 준수님처럼 `for d in new_d:` 같은 방식으로 계속 써봐야 겠습니다.

## 임준수 > 서재현

- B 1260 : 너무 깔끔한 DFS, BFS 풀이입니다!
- B 12865 : 저도 구글링 해서 풀었습니다. 제가 받은 피드백과 같이 append 안에 input을 받으면 길이를 줄일 수 있을것 같습니다.
- B 20056 : 비슷하게 접근했는데 저는 틀렸다고 나와서 참고하고 다시 풀어보겠습니다. 감사합니다!

## 서재현 > 김한주

- B 1260 :
- B 12865 :
- B 20056 :
