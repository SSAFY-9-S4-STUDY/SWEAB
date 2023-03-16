# Day13 Code Review

## 김한주 > 박원서

- S 1959 : n, m 중 큰 값을 구별하는 게 관건이었던 문제 같습니다. 저랑 거의 비슷한 방식으로 푸셨네요. 깔끔해서 보기 좋습니다 ㅎㅎ
- S 1970 : 금액별로 조건문을 따로 만들지 말고 배열을 사용하면 좀 더 깔끔하고 축약된 코드가 될 것 같습니다!
- S 4466 : 코드 깔끔해서 이해하기 좋았어요
- S 5431 : filter 함수를 쓴 제 방식과는 달리 배열을 이용하여 푸신 것 같습니다. 한 수 배워갑니다
- S 6190 : 나머지와 몫을 이용하여 단조 수를 구하셨네요. 이 문제 풀면서 한 자리 수는 단조수가 아닌가 하고 궁금했는데 pass 되신 것 보니 단조 수로 안 치나보네요.

## 김관형 > 임준수

- S 1959 : 시도(trials)한 결과를 리스트에 메모를 해줬네요. 깔끔합니다! bb 
- S 1970 : 저는 while 반복문 썼는데, 이처럼 몫과 나머지 연산을 하면 한번에 구할 수 있네요!
- S 4466 : 코드가 깔끔해서 한눈에 알아 볼 수 있었어요!
- S 5431 : `not in` 연산을 했네요! 좋습니다. 
- S 6190 : 오름차순 검사를 함수로 하셨네요! 혹시 함수 내에서 `if x[-1]==0:` 조건을 따로 써준 이유가 있을까요??


## 이장원 > 서재현

- S 1959 :
- S 1970 :
- S 4466 :
- S 5431 :
- S 6190 :


## 김주연 > 김한주

- S 1959 :
- S 1970 :
- S 4466 :
- S 5431 :
- S 6190 :

## 류동훈 > 김관형

- S 1959 : 함수를 깔끔하게 쓰셔서 보기 좋았습니다!
- S 1970 : 굳 피드백 할 게 없는 코드네요 ㅎㅎ
- S 4466 : 솔직히 문제가 쉬워서... 드릴 말씀이 없네요... 
- S 5431 : True를 활용해서 직관적으로 이해하기 쉬웠습니다.
- S 6190 : 변수 하나 하나씩 설정해서 바로 꼼꼼하게 적용하셔서 읽으면서 따라가기 편했습니다.

## 윤지현 > 이장원

- S 1959 : 두 배열의 개수 차이를 K에 할당해서 for문 돌릴 때 인덱스를 이해하기 수월하네요! (이건 취향차이 같습니다만..) `abs()`를 활용하면 코드를 보기 편하게 작성할 수는 있지만, 어차피 조건문에서 N, M의 크기를 비교하고 대소에 따라 다른 로직을 실행하기 때문에 실행에 있어서는 안해도 되는 연산을 한 번 더 해주는 것이 아닌가라는 생각이 드네요.
- S 1970 : for문에서 `enumerate`를 활용하면 조금 더 깔끔하게 코드 작성하실 수 있을 것 같아요!
- S 4466 : 코드가 아주 깔-꼼하네요.
- S 5431 : 저랑 로직도, 출력하는 방법도 똑같아서 드릴 말씀이 없네요..!
- S 6190 : 사소한 건데 if문에서 tmp랑 ans가 같을 때도 단조수인지 검증할 필요가 없기 때문에 `if tmp <= ans:`로 바꾸면 좋을 것 같아요! (제가 백트래킹을 좀 좋아해서..ㅎㅎ) 그리고 저는 뒷자리부터 한자리씩 비교했는데 정렬 활용하면 되게 쉬워지네요 배워갑니다!

## 박원서 > 김주연

- S 1959 :
- S 1970 :
- S 4466 :
- S 5431 :
- S 6190 :

## 임준수 > 류동훈

- S 1959 : 깔끔한 풀이입니다! a, b 값 활용을 잘 해주셨습니다  
- S 1970 : 빈 리스트 만들어서 계산, 출력을 깔끔하게 해주신 것 같습니다
- S 4466 : sum과 리스트 슬라이싱을 잘 활용해 주셨습니다
- S 5431 : 리스트에서 항목을 삭제하는 아이디어가 좋습니다!
- S 6190 : 이번주는 문제랑 답 다 너무 깔끔해서 적을게 많이 없네요! 고생하셨습니다

## 서재현 > 윤지현

- S 1959 : `N, M`의 부등호 방향에 따라 풀이를 다르게 설정해야 하는게 이 문제 핵심이었는데, 함수를 먼저 정의하고 조건에 따라 변수만 바꿔 넣어서 푸셨네요. 엄지척하고 갈게요.
- S 1970 : 이전부터 백트래킹을 되게 잘 활용하는 것을 보고 문제풀이에 센스가 굉장히 좋은거 같다는 인상을 받았습니다. 사실 그래서 알고리즘 수업때 남몰래 2포인트씩 내면서 지현님 SWEA 코드 한번씩 훔쳐봤었는데, 여기에서 마저도 백트래킹 어김 없으시네요.
- S 4466 : 어쩌면 `sort()`를 활용해서 무미건조하게 풀어낼 수도 있는 문제지만, 지현님은 간단한 로직을 반영해서 좀더 알고리즘답게(?) 풀어낸것 같습니다.. 잘하셨다는 말입니다. 
- S 5431 : 노코멘트 깔끔합니다.
- S 6190 : for-for문 안에서 `A[i]*A[j]`이 세번 연산되는데, 혹시 for-for문 맨 위에서 해당 연산결과를 하나의 변수에 먼저 저장하고, 그 변수를 대신 활용하셨으면 어땠을까 생각이 듭니다. 처음 스터디 문제 풀이었을텐데 앞으로 더 고생하시길 바랍니다.