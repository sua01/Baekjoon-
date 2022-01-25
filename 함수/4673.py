#22.01.25
#백준 함수 - 4673번 : 셀프 넘버


list = [0 for i in range(10000)]
x=1

while True:
    res = x
    a = x

    if(x > 1000):
        break

    while a > 0 :
        res += a%10
        a = a // 10
   
    if res<=10000:
        list[res-1] = 1

    x+=1
    if x>10000:
        break

for i in range(0, 10000):
    if list[i] != 1:
        print(i+1)
   