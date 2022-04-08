# 백준 브루트 포스 : 7568번 - 덩치

n = int(input())  # 전체 사람 수 입력받기
weight_height = []

for _ in range(n):  # 몸무게, 키 입력받기
  weight, height = map(int, input().split(' '))
  weight_height.append([weight, height])

# 자기보다 덩치 큰 사람 수 구하기
rank_list = []
for i in range(n):
  rank=0
  w = weight_height[i][0]
  h = weight_height[i][1]
  for j in range(n):
    if w < weight_height[j][0] and h < weight_height[j][1]:
      rank+=1
  rank_list.append(rank+1)

for i in rank_list:
  print(i, end=' ')

