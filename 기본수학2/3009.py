# 백준 기본수학2 : 3009번 - 네 번째 점

xNum = []
yNum = []
# 좌표 3개 입력받기
for _ in range(3):
  x, y = map(int, input().split())
  xNum.append(x)
  yNum.append(y)

for i in range(3):
  if xNum.count(xNum[i]) == 1:  #개수가 하나인 좌표 찾기
    a = xNum[i]
  if yNum.count(yNum[i]) == 1:
    b = yNum[i]

print(a,b)