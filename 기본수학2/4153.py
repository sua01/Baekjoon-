# 백준 기본수학2 : 4153번 - 직각삼각형

'''while True:
  a, b, c = map(int, input().split())

  if a == b == c == 0:
    break

  n = max(a,b,c)
  if n == a :
    if n*n == b*b + c*c:
      print('right')
    else: print('wrong')
  elif n == b :
    if n*n == a*a + c*c:
      print('right')
    else: print('wrong')
  elif n == c :
    if n*n == b*b + a*a:
      print('right')
    else: print('wrong')'''

while True:
  num = list(map(int, input().split()))

  if sum(num)==0: break # 모두 0이므로 종료

  c = max(num)  # 가장 긴 변 찾기 == 빗변
  num.remove(c) # 빗변 제외하기

  #c**2 == num[0]**2 + num[1]**2와 같음
  if c*c == num[0]*num[0] + num[1]*num[1]:  # 피타고라스 정리, 직각삼각형일 경우
    print('right')
  else: print('wrong')  #직각삼각형이 아닐 경우

