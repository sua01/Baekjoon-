# 백준 집합과 맵 : 10816번 - 숫자 카드 2
# 딕셔너리 이용

# 가지고 있는 숫자 카드 개수 n
n = int(input())

# n개의 숫자 카드에 적혀있는 정수 cards 리스트에 넣기
cards = list(map(int, input().split(' ')))

# 가지고 있는 숫자 카드와 비교할 개수 m
m = int(input())

# 가지고 있는 숫자 카드인지 구해야 할 m개의 정수
guess = list(map(int, input().split(' ')))

# 몇 개 가지고 있는 비교하기
ans = {}
for card in cards:
  if card in ans:
    ans[card] += 1
  else:
    ans[card] = 1

# 결과 출력하기
for i in guess:
  if ans.get(i) == None:
    print(0, end=' ')
  else:
    print(ans.get(i), end=' ')