# 백준 재귀 : 11729번 - 하노이 탑 이동 순서

def hanoi(n, start, tmp, to):
    if n == 1 :
        print(start, to)
    else:
        hanoi(n-1, start, to, tmp)
        print(start, to)
        hanoi(n-1, tmp, start, to)

n = int(input())

print(2**n-1)   # 옮긴 횟수
hanoi(n, 1, 2, 3) #옮기는 과정