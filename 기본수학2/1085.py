# 백준 기본수학2 : 1085번 - 직사각형에서 탈출

x, y, w, h = map(int, input().split())

'''min = 1000
min=h-y if h-y < min else min
min=w-x if w-x < min else min
min=y if y < min else min
min=x if x < min else min'''

print(min(x, y, h-y, w-x))