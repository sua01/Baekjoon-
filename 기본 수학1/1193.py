# 백준 기본수학1 : 1193번 - 분수찾기

x = int(input())

line = 0
plus = 0
while x > plus:
  line += 1
  plus += line

gap = plus - x
if line % 2 == 0: # 짝수 줄
  top = line - gap  # 분자
  under = gap + 1 # 분모
else: # 홀수 줄
  top = gap + 1 # 분자
  under = line - gap  # 분모

print(f"{top}/{under}")