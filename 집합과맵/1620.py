# 백준 집합과 맵 : 1620번 - 나는야 포켓몬 마스터 이다솜

import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # n개의 포켓몬 개수, m개의 맞춰야하는 문제 개수

# n개의 포켓몬 딕셔너리에 {번호, 포켓몬 이름}, {포켓몬 이름, 번호}입력받기
s = {}
for i in range(1, n + 1):
  pokemon = input().rstrip()
  s[i] = pokemon
  s[pokemon] = i


for i in range(m):
  quiz = input().rstrip()
  if quiz.isdigit() :  # 문제가 번호면 해당 포켓몬 이름 출력
    print(s[int(quiz)])
  else : # 문제가 알파벳이면 해당하는 번호 출력
    print(s[quiz])