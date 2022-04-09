# 백준 브루트 포스 : 1436번 - 영화감독 숌

n = int(input())  # n번째 영화 입력받기

i=0
cnt=0
while True:
  if '666' in str(i): # 666이 포함된 경우
    cnt+=1
  if cnt == n:  # n번째 영화 제목 출력
    print(i)
    break
  i+=1