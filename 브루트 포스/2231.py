# 백준 브루트 포스 : 2798번 - 분해합

n = int(input())

for i in range(n+1):
  num = list(map(int, str(i)))
  res = i + sum(num)

  if res == n:  # 생성자 있는 경우
    print(i)
    break
  
  if i == n:  # 생성자 없는 경우 0 출력
    print(0)
  
