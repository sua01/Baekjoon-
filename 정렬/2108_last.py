# 백준 정렬 : 2108번 - 통계학
import sys
from collections import Counter

num_list=[]

n = int(sys.stdin.readline())  # 홀수 n 입력받기

for _ in range(n):  # n개의 정수 입력
  num_list.append(int(sys.stdin.readline()))

# 산술평균
print(round(sum(num_list)/n))

# 중앙값
num_list.sort() # 오름차순 정렬
print(num_list[n//2])

# 최빈값
cnt = Counter(num_list).most_common()
if len(cnt) > 1 and cnt[0][1] == cnt[1][1]:
  print(cnt[1][0])
else:
  print(cnt[0][0])

# 범위
print(max(num_list)-min(num_list))