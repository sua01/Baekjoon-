# 백준 재귀 - 10872번 : 팩토리얼

# 팩토리얼 재귀 함수
def fac(n):
    if n > 1:
        return n*fac(n-1)  
    else:
        return 1

n = int(input()) # 정수 입력

print(fac(n))
