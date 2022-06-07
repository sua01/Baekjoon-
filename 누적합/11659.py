# 백준 누적 합 : 11659번 - 구간 합 구하기 4

import sys
n, m = map(int, input().split())  # 수의 개수 n, 합을 구해야 하는 횟수 m 입력받기

num = list(map(int, input().split())) # n개의 수 입력받기

for k in range(n-1):
  num[k+1] += num[k]
num = [0] + num # 맨 앞에 0 추가하기

for _ in range(m):
  # 구간 i, j 입력받기
  i, j = map(int, input().split()) 
  print(num[j] - num[i-1])