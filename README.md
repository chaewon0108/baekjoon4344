# baekjoon4344

> 1일차 2번째 문제 레츠고! (2/4)
이번 문제는 1년 반전 쯤 (샌애긔 시절...) C로 풀었다가 런타임 에러로 인해 실패로 남겨둔 문제이다.
이번에는 조금 더 공부하고 성장한 나이기 때문에 파이썬으로 다시 도전이다!!

---
# 문제
대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.

## 입력
첫째 줄에는 테스트 케이스의 개수 C가 주어진다.

둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 이어서 N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

## 출력
각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다. 정답과 출력값의 절대/상대 오차는 10-3이하이면 정답이다.

---
# 내 생각 정리
1. 케이스 개수 C 받기
2. 음계 문제와 마찬가지로 input()으로 학생수, n명의 점수 받기 -> C번만큼 반복
- split으로 분류해서 학생수와 점수 분류하기
3. 줄별로 평균을 계산 후, 평균을 넘는 학생들의 비율 계산하여 출력하기

---
# 결과
```
case_num = input()
case_num = int(case_num)

for i in range(case_num):
  info = input()
  info = info.split()
  
  student_num = int(info[0])
  score_list = list(map(int, info[1:]))
  avg = sum(score_list)/student_num
  count = 0
  for score in score_list:
    if score > avg:
      count += 1
  print(f'{count/student_num*100:.3f}%')
```

<img width="700" alt="image" src="https://github.com/chaewon0108/baekjoon4344/assets/174469937/70ff6b20-f119-497b-b6b6-947dee64dab9">


이전에 틀렸을 때랑 비교해보면, 코드 길이도 훨씬 줄었다!
음계는 조건문에서 배열의 범위를 할당하는 부분에서 잘못생각해서 조금 오래 걸렸는데, 이 문제는 10분 내로 풀렸다!
ㄴㅇㅅ~~
