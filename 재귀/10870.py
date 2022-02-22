# 백준 재귀 : 10870번 - 피보나치 수 5

# 피보나치 재귀함수
def fibo(n):
    if n == 0 : return 0
    elif n ==1 or n==2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)


n = int(input())
print(fibo(n))