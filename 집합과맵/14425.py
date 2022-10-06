# 백준 집합과 맵 : 14425번 - 문자열 집합

n, m = map(int, input().split(' '))

s = [] # n개의 문자열을 담을 리스트
for i in range(n): # n개의 문자열 입력받기
  str = input()
  s.append(str)

# m개의 검사해야하는 문자열 입력받으면서 n개의 문자열 몇 개 포함되어있는지 검사
cnt = 0 # m개의 문자열 중에 집합 S에 포함되어 있는 개수
for i in range(m):
  str = input()
  if str in s:  # 집합 s에 m개의 문자열이 포함된 경우
    cnt += 1

print(cnt)