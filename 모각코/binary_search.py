#코뮤니티 모각코 4일차 - 이분 탐색 재귀 변환

def binary_search(arr, target, start, end):
  cnt=0
  mid = (start+end)//2

  for i in arr:
    cnt+=i//mid

  if target==cnt:
    return mid
  elif target<=cnt:
    return binary_search(arr, target, mid+1, end)
  else:
    return binary_search(arr, target, start, mid-1)

  
lans=[215,513,712,803]
print(binary_search(lans, 10, 0, max(lans)))