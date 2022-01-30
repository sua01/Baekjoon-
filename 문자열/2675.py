#백준 2675 : 문자열 반복

n = int(input())
if n<0 or n>1000:
    print("잘못 입력했습니다.")


for i in range(n):
    r, s = input().split() #공백으로 구분해서 입력받기
    r = int(r)
    if (r<1 or r>8) and (len(s)<1 or len(s)>20):
        print("잘못 입력했습니다.")

    for j in range(len(s)):
        for k in range(r):
            print(s[j], end='')
    print()