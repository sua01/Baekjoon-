# 백준 집합과 맵 : 1764번 - 듣보잡

n, m = map(int, input().split())

# 듣도 못한 사람 이름 입력
names1 = []
for i in range(n):
  names1.append(input())

# 보도 못한 사람 이름 입력
names2 = []
for i in range(m):
  names2.append(input())