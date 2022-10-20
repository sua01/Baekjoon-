# 백준 집합과 맵 : 1764번 - 듣보잡

n, m = map(int, input().split())  # 듣도 못한 사람의 수, 보지 못한 사람의 수 입력받기

name1 = set()
name2 = set()

for i in range(n):
  name = input()
  name1.add(name)

for i in range(m):
  name = input()
  name2.add(name)

ans = sorted(list(name1 & name2))
print(len(ans))
for i in ans:
  print(i)