# 백준 정렬 : 2750번 - 수 정렬하기 - 버블정렬

n = int(input())  # 입력받을 개수 입력받기

num_list = []
for i in range(n):
  num_list.append(int(input()))

# 오름차순 버블 정렬
for i in range(n):
  for j in range(n):
    if num_list[i] < num_list[j]:
      num_list[i], num_list[j] = num_list[j], num_list[i]

for n in num_list:
  print(n)
