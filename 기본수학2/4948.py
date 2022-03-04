# 백준 기본수학2 : 4948번 - 베르트랑 공준

N = 123456*2+1
#에라토스테네스의 체, True이면 소수, False이면 소수 아님
num = [True]*N
for i in range(2, int(N**0.5)+1):
  if num[i]==True:
    for j in range(2*i, N, i):
      num[j] = False


while True:
  n = int(input())
  
  if n == 0 : break # 0 입력하면 종료

  cnt=0
  for i in range(n+1, 2*n+1):
    if num[i]: cnt+=1 #소수 개수 세기

  print(cnt)