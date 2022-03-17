# 모각코 8일차
# 슬라이딩 윈도우 알고리즘

caff=[0 for i in range(10)]
tau=[0 for i in range(10)]

for _ in range(10):
  x, y, z = map(int, input().split())
  caff[x] = y
  tau[x] = z

start = 0
drink_sum=0

while start<=6:
  if drink_sum < sum(tau[start:start+3])-sum(caff[start:start+3]):
    drink_sum = sum(tau[start:start+3])-sum(caff[start:start+3])
    idx = start
  start+=1

start-=1

print(f'{start} {start+1} {start+2}의 타우린 합은 {sum(tau[start:start+3])}, 카페인 합은 {sum(caff[start:start+3])}로 가장 효과가 좋습니다.')
