# 백준 재귀 : 2581번 - 소수

m = int(input())
n = int(input())

sum=0
flag = False    # 최소값 구하면 True로 바뀜

for i in range(m, n+1): 
    for j in range(2, i+1):
        if i % j == 0 :
            if j == i:
                if flag ==  False:  #소수 중 최소값 구하기
                    min = i
                    flag = True
                sum+=i
            break

if sum == 0 : # 소수가 없을 경우
    print(-1)
else:   # 소수가 있는 경우
    print(sum)
    print(min)