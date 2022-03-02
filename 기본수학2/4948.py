# 백준 재귀 : 4948번 - 베르트랑 공준

import math

def sosu(n):
  if n ==  1: return False
  for i in range(2, int(math.sqrt(n))+1):
      if n % i == 0:
        return False
  return True


n = 123456

while True:
  n = int(input())
  
  if n == 0 : break # 0 입력하면 종료

  cnt=0
  for i in range(n+1, 2*n+1):
    if sosu(i): cnt+=1

  print(cnt)