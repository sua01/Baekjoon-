#버블 정렬
#시간 복잡도 O(n^2)

arr=[5,2,9,1,6]
length = len(arr)

for i in range(length+1):
  for j in range(0, len(arr)-1-i):

    if arr[j]>arr[j+1]:
      tmp=arr[j]
      arr[j] = arr[j+1]
      arr[j+1] = tmp
      #arr[j], arr[j+1] = arr[j+1], arr[j] 와 같음

  
print(arr)
