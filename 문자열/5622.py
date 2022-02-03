#백준 5622 : 다이얼

num = input()
if len(num) < 2 and len(num) > 15:
    exit()

alph = ['ABC', "DEF", "GHI", "JKL","MNO","PQRS","TUV","WXYZ"]

time = 0
for i in range(len(num)):
    for j in alph:
        if num[i] in j: # 값 있는지 확인
            time += alph.index(j)+3

print(time)