# 백준 정렬 : 2750번 - 수 정렬하기 - 삽입정렬

n = int(input())  # 입력받을 개수 입력받기

num_list = []
for i in range(n):
  num_list.append(int(input()))

# 오름차순 삽입 정렬
for i in range(1, n):
  j = i
  while num_list[j-1] > num_list[j] and j > 0:
    num_list[j-1], num_list[j] = num_list[j], num_list[j-1]
    j -= 1


# 정렬된 리스트 출력
for n in num_list:
  print(n)
