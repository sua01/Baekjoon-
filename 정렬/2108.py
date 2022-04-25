# 백준 정렬 : 2108번 - 통계학

num_list=[]

n = int(input())  # 홀수 n 입력받기

for _ in range(n):  # n개의 정수 입력
  num = int(input())
  num_list.append(num)

# 산술평균
print(round(sum(num_list)/n))

# 중앙값
num_list.sort() # 오름차순 정렬
print(num_list[round(n/2)])

# 최빈값
dic = {}
for i in range(n):
  val = 0
  for j in range(n):
    if num_list[i] == num_list[j]:
      val +=1
  dic[num_list[i]] = val  # 빈도수 입력

all_values = dic.values()
max_val = max(all_values)

cnt = 0
for key in dic:
  if dic[key] == max_val:
    cnt+=1
    max_key = key
    if cnt == 2:
      break
print(max_key)


# 범위
print(max(num_list)-min(num_list))