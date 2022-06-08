# 백준 누적 합 : 2559번 - 수열

n, k = map(int, input().split())  # 전체 날짜 수 n, 연속적인 날짜의 수 k

temp = list(map(int, input().split()))  # 측정한 온도

temp_sum = []
temp_sum.append(sum(temp[:k]))

for i in range(n-k):
  temp_sum.append(temp_sum[i] - temp[i] + temp[k+i])

print(max(temp_sum))