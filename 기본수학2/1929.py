# 백준 기본수학2 : 1929번 - 소수 구하기
import math

m, n = map(int, input().split())

for i in range(m, n+1):
    if i ==1 : continue # 1은 소수가 아님

    k = math.sqrt(i)    # i**0.5로 제곱근 구하기 가능

    for j in range(2, int(k)+1):
        if i % j == 0:  #소수가 아닌 경우
            break

    else : print(i)  # 소수인 경우