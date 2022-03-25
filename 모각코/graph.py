# 모각코 14일차
# 그래프

arr = [[0]*4 for _ in range(4)] # 배열 생성

def insert(a, b, w, d):
  if d == 1:
    arr[a][b] = 1
    arr[b][a] = 1
  else:
    arr[a][b] = 1
  
insert(0, 1, 1, 1)
insert(0, 3, 1, 1)
insert(1, 2, 1, 1)
insert(1, 3, 1, 1)
insert(2, 3, 1, 1)

for i in range(4):
  for j in range(4):
    print(arr[i][j], end=' ')
  print()