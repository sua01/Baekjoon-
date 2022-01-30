#백준 2675 : 문자열 반복

n = input()
if n<0 or n>1000:
    print("잘못 입력했습니다.")

r, s = input().split()
if (n<1 or n>8) and (len(s)<1 or len(s)>20):
    print("잘못 입력했습니다.")