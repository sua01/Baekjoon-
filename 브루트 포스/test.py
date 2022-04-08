n = int(input())
N = list(tuple(map(int,input().split())) for _ in range(n))
answer_list = []
for i,p in enumerate(N):
    count = 0
    for j in range(n):
        if p[0] < N[j][0] and p[1] < N[j][1]:
            count += 1
    answer_list.append(count+1)
for i in answer_list:
    print(i,end=" ")