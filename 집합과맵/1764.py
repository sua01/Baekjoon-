# 백준 집합과 맵 : 1764번 - 듣보잡

n, m = map(int, input().split())

# 딕셔너리에 듣도 못한 사람의 이름, 수 입력받기
names = {}
for i in range(n):
    name = input()
    names[name] = 1

ans = []
for j in range(m):
    name = input()
    if names.get(name) == None:  
        continue
    else: # 딕셔너리에 있는 이름일 경우 듣보잡
        ans.append(name)

# 결과 출력
print(len(ans))
for answer in ans:
    print(answer)