#백준 2908 : 상수

a, b = input().split()  #공백으로 구분해서 두 수 입력받기

# 풀이 1
'''tmp = ''
for c in a:
    tmp = c + tmp
a = tmp
tmp = ''
for c in b:
    tmp = c + tmp
b = tmp

if int(a) > int(b):
    print(a)
elif int(a) < int(b):
    print(b)'''

# 풀이 2
a = int(a[::-1])
b = int(b[::-1])

print(a) if a > b  else print(b)
