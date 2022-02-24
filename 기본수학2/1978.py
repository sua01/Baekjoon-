# 백준 재귀 : 1978번 - 소수 찾기

n = int(input())

num = map(int, input().split())

cnt=0

for i in num: 
    for j in range(2, i):
        if i % j == 0 :
            cnt+=1
            continue


print(n - cnt)