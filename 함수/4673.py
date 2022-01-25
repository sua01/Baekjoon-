#22.01.25
#백준 함수 - 4673번 : 셀프 넘버

list = [0 for i in range(1000)]
x=1

while True:
    i = 1
    res = x
    a = b = x

    if(x > 1000):
        break

    while b > 0 :
        a = b % (10*i)
        b = x // (10*i)
        i*=10
        res+=a
    print(res)
    list[res-1] = 1
    x+=1

for i in range(0, len(list)-1):
    if list[i] != 1:
        print(i+1)
   