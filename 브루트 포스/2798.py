# 백준 브루트 포스 : 2798번 - 블랙잭
from itertools import combinations

n,m = map(int, input().split())

num = list(map(int, input().split()))
res = 0

'''for i in range(n):
  for j in range(i+1, n):
    for k in range(j+1, n):
      if num[i]+num[j]+num[k] <= m:   # 3개의 수의 합이 m을 넘지 않는 경우
        res = max(res, num[i]+num[j]+num[k])  # m에 최대한 가까운 카드의 합을 구함
      else:   # m을 넘은 경우
        continue'''

com = list(combinations(num, 3))
for i in com:
  if sum(i) <= m:
    res = max(res, sum(i))
print(res)