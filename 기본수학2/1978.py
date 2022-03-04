# 백준 기본수학2 : 1978번 - 소수 찾기

n = int(input())

num = map(int, input().split())

cnt=0

for i in num: 
    for j in range(2, i+1):
        if i % j == 0 :
            if j == i:
                cnt+=1
            break

print(cnt)