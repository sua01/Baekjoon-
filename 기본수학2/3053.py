# 백준 기본수학2 : 3053번 - 택시 기하학

from cmath import pi

r = int(input())

print(f'{r*r*pi : .6f}')  # f-string 이용한 반올림, 소수점 표현
print(f'{r*r*2 : .6f}')