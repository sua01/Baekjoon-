# 백준 정렬 : 2750번 - 수 정렬하기

n = int(input())  # 입력받을 개수 입력받기

num_list = []
for i in range(n):
  num_list.append(int(input()))

num_list.sort() # 오름차순 정렬

for i in range(n):
  print(num_list[i])
