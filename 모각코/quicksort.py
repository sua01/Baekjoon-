# 퀵 정렬
# 시간 복잡도 O(nlogn)

def quick_sort(arr):
  if len(arr)>1:
    pivot = arr[len(arr)-1]
    left = 0

    for right in range(len(arr)):
      if arr[right] < pivot:   # 오른쪽 값이 pivot보다 작을 경우, 왼/오 값 교환
        arr[right], arr[left] = arr[left], arr[right]
        left+=1

    # 오른쪽 포인터가 pivot에 도달했을 경우, pivot값과 왼쪽 값 교환
    arr[len(arr)-1], arr[left] = arr[left], arr[len(arr)-1]

    left_arr = quick_sort(arr[:left])
    right_arr = quick_sort(arr[left+1:])

    return left_arr+[arr[left]]+right_arr
 
  else: return arr

arr=[5,3,7,6,2,1,4]
print(quick_sort(arr))