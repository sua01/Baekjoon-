# 선택 정렬
arr = [9,6,7,3,5]
length = len(arr)

for i in range(length-1):
  min_indx = i
  for j in range(i+1, length):
    if arr[min_indx]>arr[j]:
      min_indx = j
  arr[min_indx], arr[i] = arr[i], arr[min_indx]
  print(arr)

print('정렬완료',arr)